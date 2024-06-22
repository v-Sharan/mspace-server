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
from ..logger import log


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

    # cmds.clear()

    # flag = 0
    # prev_lat, prev_lon = 0, 0
    # cmds.add(
    #     Command(
    #         0,
    #         0,
    #         0,
    #         mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
    #         mavutil.mavlink.MAV_CMD_NAV_VTOL_TAKEOFF,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         30,
    #     )
    # )
    # cmds.add(
    #     Command(
    #         0,
    #         0,
    #         0,
    #         mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
    #         mavutil.mavlink.MAV_CMD_NAV_VTOL_TAKEOFF,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         0,
    #         30,
    #     )
    # )
    # with open(
    #     "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/csvs/forward-drone-"
    #     + str(i + 1)
    #     + ".csv",
    #     "r",
    # ) as f:
    #     csvreader = csv.reader(f)
    #     for row in csvreader:
    #         lat = float(row[0])
    #         lon = float(row[1])
    #         if not flag:
    #             cmds.add(
    #                 Command(
    #                     0,
    #                     0,
    #                     0,
    #                     mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
    #                     mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     lat,
    #                     lon,
    #                     altitude,
    #                 )
    #             )
    #             cmds.add(
    #                 Command(
    #                     0,
    #                     0,
    #                     0,
    #                     mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
    #                     mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     lat,
    #                     lon,
    #                     altitude,
    #                 )
    #             )
    #         else:
    #             cmds.add(
    #                 Command(
    #                     0,
    #                     0,
    #                     0,
    #                     mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
    #                     mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     0,
    #                     lat,
    #                     lon,
    #                     altitude,
    #                 )
    #             )
    #         prev_lat = lat
    #         prev_lon = lon
    #         flag = 1
    #     cmds.add(
    #         Command(
    #             0,
    #             0,
    #             0,
    #             mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
    #             mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #             0,
    #             prev_lat,
    #             prev_lon,
    #             altitude,
    #         )
    #     )
    print(" Clear any existing commands")
    cmds.clear()

    print(" Define/add new commands.")
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
    with open(
        "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/csvs/forward-drone-"
        + str(i + 1)
        + ".csv",
        "r",
    ) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            print(row)
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
    with open(
        "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/csvs/search-drone-"
        + str(i + 1)
        + ".csv",
        "r",
    ) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            print(row)
            lat = float(row[0])
            lon = float(row[1])
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

    with open(
        "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/csvs/reverse-drone-"
        + str(i + 1)
        + ".csv",
        "r",
    ) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            print(row)
            lat = float(row[0])
            lon = float(row[1])
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
def Connect_vehicles():
    vehicles = []
    print("Connectingggggggg")
    for i in range(1, 9):
        try:
            port = "udpin:192.168.6.215:1455" + str(i)
            vehicle = connect(port, heartbeat_timeout=10)
            vehicles.append(vehicle)
            print("vehicle Connecting")
            log.info("vehicle {} is connected {}".format(i, vehicle))
        except:
            # vehicles.append(0)
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
