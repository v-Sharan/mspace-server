import time


def Skip_waypoint(vehicles, pointNumber):
    print(vehicles)
    for vehicle in vehicles:
        nextwaypoint = vehicle.commands.next
        vehicle.commands.next = pointNumber
        time.sleep(0.2)
    return True
