#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
© Copyright 2015-2016, 3D Robotics.
mission_basic.py: Example demonstrating basic mission operations including creating, clearing and monitoring missions.

Full documentation is provided at https://dronekit-python.readthedocs.io/en/latest/examples/mission_basic.html
"""
from __future__ import print_function

from dronekit import (
    connect,
    LocationGlobalRelative,
    LocationGlobal,
    Command,
)
import time
import math, csv, subprocess, os
from pymavlink import mavutil


def get_location_metres(original_location, dNorth, dEast):
    """
    Returns a LocationGlobal object containing the latitude/longitude `dNorth` and `dEast` metres from the
    specified `original_location`. The returned Location has the same `alt` value
    as `original_location`.

    The function is useful when you want to move the vehicle around specifying locations relative to
    the current vehicle position.
    The algorithm is relatively accurate over small distances (10m within 1km) except close to the poles.
    For more information see:
    http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters
    """
    earth_radius = 6378137.0  # Radius of "spherical" earth
    # Coordinate offsets in radians
    dLat = dNorth / earth_radius
    dLon = dEast / (earth_radius * math.cos(math.pi * original_location.lat / 180))

    # New position in decimal degrees
    newlat = original_location.lat + (dLat * 180 / math.pi)
    newlon = original_location.lon + (dLon * 180 / math.pi)
    return LocationGlobal(newlat, newlon, original_location.alt)


def get_distance_metres(aLocation1, aLocation2):
    """
    Returns the ground distance in metres between two LocationGlobal objects.

    This method is an approximation, and will not be accurate over large distances and close to the
    earth's poles. It comes from the ArduPilot test code:
    https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
    """
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat * dlat) + (dlong * dlong)) * 1.113195e5


def distance_to_current_waypoint(vehicle):
    """
    Gets distance in metres to the current waypoint.
    It returns None for the first waypoint (Home location).
    """
    nextwaypoint = vehicle.commands.next
    if nextwaypoint == 0:
        return None
    missionitem = vehicle.commands[nextwaypoint - 1]  # commands are zero indexed
    lat = missionitem.x
    lon = missionitem.y
    alt = missionitem.z
    targetWaypointLocation = LocationGlobalRelative(lat, lon, alt)
    distancetopoint = get_distance_metres(
        vehicle.location.global_frame, targetWaypointLocation
    )
    return distancetopoint


def adds_square_mission(vehicle, i, altitude):
    """
    Adds a takeoff command and four waypoint commands to the current mission.
    The waypoints are positioned to form a square of side length 2*aSize around the specified LocationGlobal (aLocation).

    The function assumes vehicle.commands matches the vehicle mission state
    (you must have called download at least once in the session and after clearing the mission)
    """

    cmds = vehicle.commands

    cmds.clear()

    flag = 0
    prev_lat, prev_lon = 0, 0
    cmds.add(
        Command(
            0,
            0,
            0,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_VTOL_TAKEOFF,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            30,
        )
    )
    cmds.add(
        Command(
            0,
            0,
            0,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_VTOL_TAKEOFF,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            30,
        )
    )
    with open(
        "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/csvs/forward-drone-"
        + str(i + 1)
        + ".csv",
        "r",
    ) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            lat = float(row[0])
            lon = float(row[1])
            if not flag:
                cmds.add(
                    Command(
                        0,
                        0,
                        0,
                        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                        mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        lat,
                        lon,
                        altitude,
                    )
                )
                cmds.add(
                    Command(
                        0,
                        0,
                        0,
                        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                        mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        lat,
                        lon,
                        altitude,
                    )
                )
            else:
                cmds.add(
                    Command(
                        0,
                        0,
                        0,
                        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                        mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        lat,
                        lon,
                        altitude,
                    )
                )
            prev_lat = lat
            prev_lon = lon
            flag = 1
        cmds.add(
            Command(
                0,
                0,
                0,
                mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM,
                0,
                0,
                0,
                0,
                0,
                0,
                prev_lat,
                prev_lon,
                altitude,
            )
        )
    cmds.upload()
    vehicle.close()


def ping(self, host):
    """
    Ping a host to check for network connectivity.
    Returns True if the host responds to ping, False otherwise.
    """
    try:
        subprocess.check_call(["ping", "-n", "1", host])
        return True
    except subprocess.CalledProcessError:
        return False


# def Connect_vehicles(drones, ip_address):
def Connect_vehicles(log):
    vehicles = []
    # heartbeat_ip_address = [
    #     "192.168.6.101",
    #     "192.168.6.102",
    #     "192.168.6.103",
    #     "192.168.6.104",
    #     "192.168.6.105",
    #     "192.168.6.106",
    #     "192.168.6.107",
    #     "192.168.6.108",
    #     "192.168.6.109",
    #     "192.168.6.110",
    #     "192.168.6.111",
    #     "192.168.6.112",
    #     "192.168.6.113",
    #     "192.168.6.114",
    #     "192.168.6.115",
    # ]
    # heartbeat_ip = [0] * 20

    # port = 14551

    # for i in range(len(heartbeat_ip_address)):
    #     response = ping(heartbeat_ip_address[i])
    #     if response:
    #         heartbeat_ip[i] = 30
    #     else:
    #         heartbeat_ip[i] = 2

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle1 = connect(serialport, heartbeat_timeout=heartbeat_ip[0])
    #     print(serialport)
    #     vehicles.append(vehicle1)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1
    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle2 = connect(serialport, heartbeat_timeout=heartbeat_ip[1])
    #     print(serialport)

    #     vehicles.append(vehicle2)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1
    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle3 = connect(serialport, heartbeat_timeout=heartbeat_ip[2])
    #     print(serialport)
    #     vehicles.append(vehicle3)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle4 = connect(serialport, heartbeat_timeout=heartbeat_ip[3])
    #     print(serialport)
    #     vehicles.append(vehicle4)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1

    # try:
    #     serialport = "udpin:" + str(ip_address) + "" + ":" + str(port)
    #     vehicle5 = connect(serialport, heartbeat_timeout=heartbeat_ip[4])
    #     print(serialport)
    #     vehicles.append(vehicle5)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle6 = connect(serialport, heartbeat_timeout=heartbeat_ip[5])
    #     print(serialport)
    #     vehicles.append(vehicle6)
    # except:

    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle7 = connect(serialport, heartbeat_timeout=heartbeat_ip[6])
    #     print(serialport)
    #     vehicles.append(vehicle7)
    # except:

    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle8 = connect(serialport, heartbeat_timeout=heartbeat_ip[7])
    #     print(serialport)
    #     vehicles.append(vehicle8)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle9 = connect(serialport, heartbeat_timeout=heartbeat_ip[8])
    #     print(serialport)
    #     vehicles.append(vehicle9)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # port += 1

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle10 = connect(serialport, heartbeat_timeout=heartbeat_ip[9])
    #     print(serialport)
    #     vehicles.append(vehicle10)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle11 = connect(serialport, heartbeat_timeout=heartbeat_ip[10])
    #     print(serialport)
    #     vehicles.append(vehicle11)

    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle12 = connect(serialport, heartbeat_timeout=heartbeat_ip[11])
    #     print(serialport)
    #     vehicles.append(vehicle12)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle13 = connect(serialport, heartbeat_timeout=heartbeat_ip[12])
    #     print(serialport)
    #     vehicles.append(vehicle13)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle14 = connect(serialport, heartbeat_timeout=heartbeat_ip[13])
    #     print(serialport)
    #     vehicles.append(vehicle14)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle15 = connect(serialport, heartbeat_timeout=heartbeat_ip[14])
    #     print(serialport)
    #     vehicles.append(vehicle15)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return

    # try:
    #     serialport = "udpin:" + str(ip_address) + ":" + str(port)
    #     vehicle16 = connect(serialport, heartbeat_timeout=heartbeat_ip[15])
    #     vehicles.append(vehicle16)
    # except:
    #     pass

    # if len(vehicles) >= drones:
    #     return
    try:
        vehicle1 = connect("udpin:192.168.6.215:14551", heartbeat_timeout=10)
        vehicles.append(vehicle1)
        log.info("vehicle 1 is connected {}".format(vehicle1))
    except:
        pass
    try:
        vehicle2 = connect("udpin:192.168.6.215:14552", heartbeat_timeout=10)
        vehicles.append(vehicle2)
        log.info("vehicle 2 is connected {}".format(vehicle2))
    except:
        pass
    try:
        vehicle3 = connect("udpin:192.168.6.215:14553", heartbeat_timeout=10)
        vehicles.append(vehicle3)
        log.info("vehicle 3 is connected {}".format(vehicle3))
    except:
        pass
    print(vehicles)
    return vehicles


def main():
    from ..socket.globalVariable import get_vehicle

    vehicles = get_vehicle()
    index = 0
    alt = 100
    for vehicle in vehicles:
        adds_square_mission(vehicle, index, alt)
        index += 1
        alt += 25
