#!/usr/bin/python2.7
from __future__ import print_function
from __future__ import division

import math
import time
import select
import numpy as np
import bluetooth
import rospy
from sensor_msgs.msg import LaserScan

# import sys
np.set_printoptions(suppress=True,linewidth=np.nan,threshold=np.nan)

SCAN_MSG_TOPIC = "/scan"

SCAN_BT_MSG = None

def check_bluetooth_request():
    return True

def scan_cb(msg):
    global SCAN_BT_MSG
    ranges = msg.ranges
    # convert scan to a compact and useful message
    scan_bytes = np.uint32(len(ranges)).tobytes()
    ang_start_rad_bytes = np.float32(msg.angle_min).tobytes()
    ang_inc_rad_bytes = np.float32(msg.angle_increment).tobytes()
    ranges_u8_bytes = convert_ranges_to_u8_msg(ranges)
    bt_msg = scan_bytes + ang_start_rad_bytes + ang_inc_rad_bytes + ranges_u8_bytes
    # print("scan points:", len(ranges_u8_bytes))
    # print("complete message len", len(bt_msg), "(should be scan points + 12)")
    SCAN_BT_MSG = bt_msg



def convert_ranges_to_u8_msg(ranges):
    '''
    Msg format: uint8 for each distance in ranges.

    Each 1 unit of this uint8 distance is equal to 1/50th meter (2cm),
        up to a max of 255 units or 5.12 meters

    Any distances > 255 are set to 0.
    Any unknown distances are set to 0.
    thus, ignore the zeros.
    '''
    ranges_unit = np.floor(np.array(ranges)*50) # 1 meter => 50 unit, max is 255 unit (5.12m), ignore the zeros (outlier or unknown)
    ranges_unit[(ranges_unit > 255) | (ranges_unit < 0)] = 0
    ranges_unit = np.array(ranges_unit, dtype='uint8')
    return ranges_unit.tobytes()



if __name__ == '__main__':
    rospy.init_node('bluetooth_bridge', disable_signals=True)
    rospy.Subscriber(SCAN_MSG_TOPIC, LaserScan, scan_cb, queue_size=1)


    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM )
    server_sock.bind(("",bluetooth.PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = '023f3c7f-af05-4299-bd2d-52487cb6cef7'
    bluetooth.advertise_service( server_sock, "LidarServer",
                   service_id = uuid,
                   service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
                   profiles = [ bluetooth.SERIAL_PORT_PROFILE ]
                   )

    client_sock = None

    try:
        while True:
            rospy.sleep(1)
            print("Waiting for connection on RFCOMM channel %d" % port)
            client_sock, client_info = server_sock.accept()
            print("Accepted connection from ", client_info)
            client_sock.setblocking(0)
            try:
                while True:
                    ready = select.select([client_sock], [], [], 0.01)
                    if ready[0] and SCAN_BT_MSG is not None:
                        data = client_sock.recv(1024)
                        # if len(data) == 0: break
                        print("received [%s]" % data)
                        client_sock.send(SCAN_BT_MSG)
                    rospy.sleep(0.05)
            except IOError:
                pass

    except KeyboardInterrupt:
        pass

    print("disconnected")
    if client_sock is not None: client_sock.close()
    server_sock.close()
    print("all done")

