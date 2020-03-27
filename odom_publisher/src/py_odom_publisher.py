#!/usr/bin/env python

import math
from math import sin, cos, pi

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

import py_odom_func
import time

rospy.init_node('odometry_publisher')
#setup ros odometry for camera on odom_in topic

odom_pub = rospy.Publisher("odom_in", Odometry, queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()

d1 = py_odom_func.d2_odom(0,0,0)
location = py_odom_func.robot_loc(0,0,0)
l =1

current_time = rospy.Time.now()
last_time = rospy.Time.now()
ts = time.time()
to = 0
r = rospy.Rate(1.0)

print('J5 odom interace strarted')
while not rospy.is_shutdown():
    #this is where the data is taken in 
    vr =0
    vl =0
    ti = time.time()-ts

    # compute odometry in a typical way given the velocities of the robot
    li = location 
    d1= py_odom_func.d2_odom(vr,vl,ti)

    #calculate velocities 
    vth = 1/l *(d1.vr-d1.vl)
    vx = .5*(d1.vr+d1.vl)
    vy = .5*(d1.vr+d1.vl)
    
    #calc odom
    location.thet = py_odom_func.integrate(vth,li.thet,ti,to)
    location.x = py_odom_func.integrate(vx,li.x,ti,to)*math.cos(location.thet)
    location.y = py_odom_func.integrate(vy,li.y,ti,to)*math.sin(location.thet)
   
    # since all odometry is 6DOF we'll need a quaternion created from yaw
    odom_quat = tf.transformations.quaternion_from_euler(0, 0, location.thet)

    # first, we'll publish the transform over tf
    odom_broadcaster.sendTransform(
        (location.x, location.y, 0.),
        odom_quat,
        current_time,
        "base_link",
        "odom_in"
    )

    # next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom_in"

    # set the position
    odom.pose.pose = Pose(Point(location.x, location.y, 0.), Quaternion(*odom_quat))

    # set the velocity
    odom.child_frame_id = "base_link"
    odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

    # publish the message
    odom_pub.publish(odom)
    to=ti
    last_time = current_time 
    location.print_location()
    r.sleep()
