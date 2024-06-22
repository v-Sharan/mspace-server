from time import sleep
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)

sys.path.append(parent_directory)

from siyi_sdk.siyi_sdk import SIYISDK

prev_yaw = 0
prev_pitch = 0


def main(up, down, right, left):

    global prev_yaw, prev_pitch

    cam = SIYISDK(server_ip="192.168.6.141", port=37260)
    if not cam.connect():
        print("No connection ")
        exit(1)

    if up == 1:
        pitch = prev_pitch + 4
        cam.setGimbalRotation(prev_yaw, pitch)
    if down == 1:
        pitch = prev_pitch - 4
        cam.setGimbalRotation(prev_yaw, pitch)
    if right == 1:
        yaw = prev_yaw + 4
        cam.setGimbalRotation(yaw, prev_pitch)
    if left == 1:
        yaw = prev_yaw - 4
        cam.setGimbalRotation(yaw, prev_pitch)

    print("Attitude (yaw,pitch,roll) eg:", cam.getAttitude())

    cam.disconnect()
