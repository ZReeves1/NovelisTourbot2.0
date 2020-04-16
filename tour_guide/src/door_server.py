#! /usr/bin/env python

from tour_guide.srv import opendoor
import rospy

def handle_door(req):
    rospy.loginfo('sending open door command to door %s', req.door_id)
    return True

def door_server():
    rospy.init_node('door_server')
    s = rospy.Service('door', opendoor, handle_door)
    rospy.loginfo("ready to open doors ")
    rospy.spin()

if __name__ == "__main__":
    door_server()
