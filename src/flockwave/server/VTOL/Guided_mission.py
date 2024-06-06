import math


def destination_location(homeLattitude, homeLongitude, distance, bearing):
    R = 6371e3  # Radius of earth in metres
    rlat1 = homeLattitude * (math.pi / 180)
    rlon1 = homeLongitude * (math.pi / 180)
    d = distance
    bearing = bearing * (math.pi / 180)
    rlat2 = math.asin(
        (math.sin(rlat1) * math.cos(d / R))
        + (math.cos(rlat1) * math.sin(d / R) * math.cos(bearing))
    )
    rlon2 = rlon1 + math.atan2(
        (math.sin(bearing) * math.sin(d / R) * math.cos(rlat1)),
        (math.cos(d / R) - (math.sin(rlat1) * math.sin(rlat2))),
    )
    rlat2 = rlat2 * (180 / math.pi)
    rlon2 = rlon2 * (180 / math.pi)
    location = [rlat2, rlon2]
    return location


def Guided_Mission(t_lat, t_lon):
    lat_lon1 = destination_location(t_lat, t_lon, float(500), float(-90))
    lat1, lon1 = lat_lon1[0], lat_lon1[1]
    lat_lon2 = destination_location(t_lat, t_lon, float(500), float(90))
    lat2, lon2 = lat_lon2[0], lat_lon2[1]

    result = []

    result.append([lat1, lon1])
    result.append([lat2, lon2])

    print(result)
    return result


# t_lat, t_lon = 13.389466, 80.234221
# Guided_Mission(t_lat, t_lon)
