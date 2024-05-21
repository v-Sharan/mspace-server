import simplekml

# import mission_basic_1 as MB
from .new_left import main as VPL
from .new_Right import main as VPR

original_location = []
R = 6373.0
home_location = None


def download_mission(vehicles):
    lat_lon = []
    for vehicle in vehicles:
        print(vehicle)
        missionlist = []
        cmds = vehicle.commands
        cmds.download()
        cmds.wait_ready()
        vehicle.parameters.wait_ready()
        for cmd in cmds:
            print(cmd)
            if int(cmd.x) == 0:
                continue
            missionlist.append([cmd.y, cmd.x])
        lat_lon.append(missionlist)
    return lat_lon


def download_mission_kml(kml_file, vehicle, sys_id):
    kml = simplekml.Kml()
    missionlist = []
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()
    vehicle.parameters.wait_ready()
    i = 1
    for cmd in cmds:
        if int(cmd.x) == 0:
            continue
        missionlist.append([cmd.x, cmd.y, cmd.z])
        kml.newpoint(name="{}_{}".format(sys_id, i), coords=[(cmd.y, cmd.x, cmd.z)])
        i += 1
    kml.save(kml_file)


def clear_mission(vehicle):
    cmds = vehicle.commands
    cmds.clear()
    cmds.upload()


def main(selected_turn, numOfDrones):
    from ..socket.globalVariable import get_vehicle

    index = 1
    vehicles = get_vehicle()
    vehicle = vehicles[0]

    sys_id = index
    download_mission_kml(
        "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/Mission.kml",
        vehicle,
        sys_id,
    )
    if selected_turn == "left":
        VPL(numOfDrones, "192.168.0.127")
    elif selected_turn == "right":
        VPR(numOfDrones, "192.168.0.127")

    return True
