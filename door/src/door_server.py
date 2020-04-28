#! /usr/bin/env python

from door.srv import opendoor
import rospy
from EmulatorGUI import GPIO
import time

def handle_door(req):
    rospy.loginfo('sending open door command to door %s', req.door_id)
    if req.door_id == 1:
    	GPIO.output(2,GPIO.HIGH)
    	time.sleep(1)
    	GPIO.output(2,GPIO.LOW)
    elif req.door_id ==2:
    	GPIO.output(3,GPIO.HIGH)
    	time.sleep(1)
    	GPIO.output(3,GPIO.LOW)
    elif req.door_id == 3:
    	GPIO.output(4,GPIO.HIGH)
    	time.sleep(1)
    	GPIO.output(4,GPIO.LOW)
    
    return True

def door_server():
    rospy.init_node('door_server')
    s = rospy.Service('door', opendoor, handle_door)
    rospy.loginfo("ready to open doors ")
    rospy.spin()

if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
 
        GPIO.setwarnings(False)
 
        GPIO.setup(2, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(3, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(4, GPIO.OUT, initial = GPIO.LOW)
        
        door_server()
    except Exception as ex:
        traceback.print_exc()
    finally:
        GPIO.cleanup() #this ensures a clean exit
 
