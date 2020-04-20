#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#import tf.transformations
from geometry_msgs.msg import Twist
import json

incr = 0
def callback(msg):

    global incr
    incr = incr +1
    # callback is where the action happens here we print the keyboard commands to the console
    rospy.loginfo("Received a /cmd_vel message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
    rospy.loginfo("count: %d"%(incr))
	#movement is a python object containing the labels and data

    
    movement = { 
        "x": msg.linear.x, 
        "y": msg.linear.y, 
        "z": msg.linear.z, 
        "ax": msg.angular.x, 
        "ay": msg.angular.y, 
        "az": msg.angular.z,
        "inc":incr
    }
    with open("movmentcommand.json","w") as write_file:
        json.dump(movement,write_file)
   	
    y = json.dumps(movement)
    

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    
    rospy.init_node('listener', anonymous=True)
#create the subscriber and tell it to expect a twist
    rospy.Subscriber("cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
