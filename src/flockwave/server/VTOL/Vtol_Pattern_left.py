import math
from scipy import interpolate
import simplekml
import xml.etree.ElementTree as ET
import csv
import os
import math
from scipy import interpolate
from .mission_basic_1 import main as MB


def destination_location(homeLattitude, homeLongitude, distance, bearing):
    R = 6371e3  # Radius of earth in metres
    rlat1 = homeLattitude * (math.pi / 180)
    rlon1 = homeLongitude * (math.pi / 180)
    d = distance
    bearing = bearing * (math.pi / 180)  # Converting bearing to radians
    rlat2 = math.asin(
        (math.sin(rlat1) * math.cos(d / R))
        + (math.cos(rlat1) * math.sin(d / R) * math.cos(bearing))
    )
    rlon2 = rlon1 + math.atan2(
        (math.sin(bearing) * math.sin(d / R) * math.cos(rlat1)),
        (math.cos(d / R) - (math.sin(rlat1) * math.sin(rlat2))),
    )
    rlat2 = rlat2 * (180 / math.pi)  # Converting to degrees
    rlon2 = rlon2 * (180 / math.pi)  # converting to degrees
    location = [rlat2, rlon2]
    return location


def gps_bearing(
    homeLattitude, homeLongitude, destinationLattitude, destinationLongitude
):
    R = 6371e3  # Radius of earth in metres
    rlat1 = homeLattitude * (math.pi / 180)
    rlat2 = destinationLattitude * (math.pi / 180)
    rlon1 = homeLongitude * (math.pi / 180)
    rlon2 = destinationLongitude * (math.pi / 180)
    dlat = (destinationLattitude - homeLattitude) * (math.pi / 180)
    dlon = (destinationLongitude - homeLongitude) * (math.pi / 180)
    # haversine formula to find distance
    a = (math.sin(dlat / 2) * math.sin(dlat / 2)) + (
        math.cos(rlat1) * math.cos(rlat2) * (math.sin(dlon / 2) * math.sin(dlon / 2))
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # distance in metres
    # formula for bearing
    y = math.sin(rlon2 - rlon1) * math.cos(rlat2)
    x = math.cos(rlat1) * math.sin(rlat2) - math.sin(rlat1) * math.cos(
        rlat2
    ) * math.cos(rlon2 - rlon1)
    bearing = math.atan2(y, x)  # bearing in radians
    bearingDegrees = bearing * (180 / math.pi)
    out = [distance, bearingDegrees]
    return out


def extract_data_from_kml(kml_file_path):
    # Open the KML file
    kml = simplekml.Kml()
    kml.open(kml_file_path)

    # Access features in the KML file
    for feature in kml.features():
        # Check if the feature is a placemark
        if isinstance(feature, simplekml.Placemark):
            placemark = feature
            # Extract placemark data
            name = placemark.name
            description = placemark.description
            coordinates = (
                placemark.geometry.coords
            )  # Coordinates in (longitude, latitude) format
            print("Name:", name)
            print("Description:", description)
            print("Coordinates:", coordinates)
            print("----------------------------------")


def kml_read(kml_file_path):
    tree = ET.parse(kml_file_path)
    root = tree.getroot()
    # result_array = [["latitude","longitude"]]
    result_array = []

    for placemark in root.findall(".//{http://www.opengis.net/kml/2.2}Placemark"):
        name = placemark.find("{http://www.opengis.net/kml/2.2}name").text
        coordinates = placemark.find(
            ".//{http://www.opengis.net/kml/2.2}coordinates"
        ).text
        coordinates_list = coordinates.strip().split(" ")

        for coordinate_set in coordinates_list:
            lon, lat, alt = map(float, coordinate_set.split(","))
            result_array.append([lat, lon])

    return result_array


def cartToGeo(origin, endDistance, cartLocation):
    # The initial point of rectangle in (x,y) is (0,0) so considering the current
    # location as origin and retreiving the latitude and longitude from the GPS
    # origin = (12.948048, 80.139742) Format

    # Calculating the hypot end point for interpolating the latitudes and longitudes
    rEndDistance = math.sqrt(2 * (endDistance**2))

    # The bearing for the hypot angle is 45 degrees considering coverage area as square
    bearing = 45

    # Determining the Latitude and Longitude of Middle point of the sqaure area
    # and hypot end point of square area for interpolating latitude and longitude
    lEnd, rEnd = destination_location(
        origin[0], origin[1], rEndDistance, 180 + bearing
    ), destination_location(origin[0], origin[1], rEndDistance, bearing)

    # Array of (x,y)
    x_cart, y_cart = [-endDistance, 0, endDistance], [-endDistance, 0, endDistance]

    # Array of (latitude, longitude)
    x_lon, y_lat = [lEnd[1], origin[1], rEnd[1]], [lEnd[0], origin[0], rEnd[0]]

    # Latitude interpolation function
    f_lat = interpolate.interp1d(y_cart, y_lat)

    # Longitude interpolation function
    f_lon = interpolate.interp1d(x_cart, x_lon)

    # Converting (latitude, longitude) to (x,y) using interpolation function
    lat, lon = f_lat(cartLocation[1]), f_lon(cartLocation[0])
    return (lat, lon)


def generate_XY_Positions(numOfDrones, x, y, origin):
    endDistance = 10000
    Initial_x, Initial_y = x, y
    XY_values = []
    lat, lon = cartToGeo(origin, endDistance, [0, 0])
    XY_values.append([lat, lon])
    for i in range(numOfDrones - 1):
        lat, lon = cartToGeo(origin, endDistance, [Initial_x, Initial_y])
        XY_values.append([lat, lon])
        Initial_x += x
        Initial_y += y
    return XY_values


def main(Drones, ip_address):

    result = kml_read(
        "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/Mission.kml"
    )

    numOfDrones = Drones

    bearing = 0
    prev_bearing = 0

    x = 120
    y = 120

    flag = 0

    lat_lons = [[], [], []]

    for index in range(len(result)):

        res = generate_XY_Positions(numOfDrones, x, y, result[index])
        print(res)
        if flag:
            for i in range(len(res)):
                bearing = abs(
                    gps_bearing(
                        lat_lons[i][-1][0],
                        lat_lons[i][-1][1],
                        res[i][0],
                        res[i][1],
                    )[1]
                )

                if (
                    prev_bearing >= -30
                    and prev_bearing <= 30
                    and bearing >= 50
                    and bearing <= 125
                ):
                    x = 120
                    y = -120
                elif (
                    prev_bearing >= 50
                    and prev_bearing <= 125
                    and bearing >= 150
                    and bearing <= 210
                ):
                    x = 120
                    y = 120
                elif (
                    prev_bearing >= 150
                    and prev_bearing <= 210
                    and bearing >= 50
                    and bearing <= 125
                ):
                    x = -120
                    y = 120
                elif (
                    prev_bearing >= 50
                    and prev_bearing <= 125
                    and bearing >= -30
                    and bearing <= 30
                ):
                    x = -120
                    y = -120
            prev_bearing = bearing
        else:
            for i in range(len(res)):
                bearing = abs(
                    gps_bearing(
                        result[index][0],
                        result[index][1],
                        res[i][0],
                        res[i][1],
                    )[1]
                )
                prev_bearing = bearing
        res = generate_XY_Positions(numOfDrones, x, y, result[index])
        # print(res)
        for i in range(len(res)):
            lat_lons[i].append(res[i])
        flag = 1

    for i in range(numOfDrones):
        with open(
            "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/csvs/forward-drone-"
            + str(i + 1)
            + ".csv",
            "w",
            newline="",
        ) as f:
            csvwriter = csv.writer(f)
            for j in range(len(lat_lons[i])):
                csvwriter.writerow([lat_lons[i][j][0], lat_lons[i][j][1]])

    # for i in range(numOfDrones):
    #     with open(
    #         "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/csvs/reverse-drone-" + str(i + 1) + ".csv",
    #         "w",
    #         newline="",
    #     ) as f:
    #         csvwriter = csv.writer(f)
    #         for j in range(len(lat_lons[i]) - 1, -1, -1):
    #             csvwriter.writerow([lat_lons[i][j][0], lat_lons[i][j][1]])
    MB()
