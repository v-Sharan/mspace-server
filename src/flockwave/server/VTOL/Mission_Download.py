import simplekml

# import mission_basic_1 as MB
from .new_left import main as VPL
from .new_Right import main as VPR
from dronekit import connect

original_location = []
R = 6373.0
home_location = None


def download_mission(vehicles):
    from ..socket.globalVariable import saveDownload, downloadMission

    mission = downloadMission()
    if len(mission) > 0:
        print(mission)
        return mission
    lat_lon = []
    for vehicle in vehicles:
        print(vehicle)
        missionlist = []
        cmds = vehicle.commands
        cmds.download()
        cmds.wait_ready()
        vehicle.parameters.wait_ready()
        for cmd in cmds:
            # print(cmd)
            if int(cmd.x) == 0:
                continue
            missionlist.append([cmd.y, cmd.x])
        lat_lon.append(missionlist)

    saveDownload(lat_lon)
    return lat_lon


def download_mission_kml(kml_file, kml_file1, vehicle, sys_id):
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
    i = 1
    kml1 = simplekml.Kml()
    missionlist = missionlist[::-1]
    for command in missionlist:
        if int(cmd.x) == 0:
            continue
        kml.newpoint(
            name="{}_{}".format(sys_id, i),
            coords=[(command[0], command[1], command[2])],
        )
        i += 1
    kml1.save(kml_file1)


def clear_mission(vehicle):
    cmds = vehicle.commands
    cmds.clear()
    cmds.upload()


def main(selected_turn, numOfDrones):
    from ..socket.globalVariable import get_vehicle

    index = 1
    vehicles = get_vehicle()
    print(vehicles)
    vehicle = connect("udpin:192.168.6.215:14551", heartbeat_timeout=10)

    sys_id = index
    download_mission_kml(
        "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/Forward-Mission.kml",
        "C:/Users/vshar/OneDrive/Documents/fullstack/skybrush-server/src/flockwave/server/VTOL/Reverse-Mission.kml",
        vehicle,
        sys_id,
    )
    if selected_turn == "left":
        VPL(numOfDrones)
    elif selected_turn == "right":
        VPR(numOfDrones)

    return True
