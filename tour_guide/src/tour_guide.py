#! /usr/bin/env python

#this is the client for controling the novelis tour bot

import rospy
import actionlib
import json
import cv2
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

class tour():
 
  def read_locations(self,filename):
    with open(filename,'r') as l:
      locations= json.load(l)
      rospy.loginfo(locations)
    #read in location list
    #l = '{"origin":{"x": 0.0,"y":0.0,"rz":0.0},"loc1":{"x": 1.0,"y":2.0,"rz":3.0}}'
    #locations= json.loads(l)
    return locations


  def __init__(self):
    argv= rospy.myargv(argv=sys.argv)
    fname = argv[1]
    locations = self.read_locations(fname)
    rospy.init_node('tour',anonymous = False)
    
    for i in locations:
      rospy.loginfo("moving to %s",i.get("name"))
      self.goalReached = self.moveToGoal(i.get("x"), i.get("y"),i.get("rz"))
 
  def shutdown(self):
    #stop the program at the end of tour
    rospy.loginfo("quit program")
    rospy.sleep()
  
  def moveToGoal(self,x,y,rz):
    #define a client to send movement commands to the movebase server 
    ac =actionlib.SimpleActionClient("move_base", MoveBaseAction)
    
    while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
      rospy.loginfo("waiting for server")
    goal = MoveBaseGoal()
    
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    
    goal.target_pose.pose.position = Point(x,y,0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = rz
    goal.target_pose.pose.orientation.w = 1.0
   
    rospy.loginfo("Sending goal location")
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(120))

    if(ac.get_state()== GoalStatus.SUCCEEDED):
      rospy.loginfo("reached goal")
      return True
    else:
      rospy.loginfo("the robot failed to reach the goal")
      return False
 
  def play_vid(self,vidpath):

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture(vidpath)

    # Check if camera opened successfully
    if (cap.isOpened()== False): 
      print("Error opening video stream or file")
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = frames/fps
    cv2.namedWindow('Frame')
    rospy.sleep(duration)
    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
      ret, frame = cap.read()
      if ret == True:
	# Display the resulting frame
        cv2.imshow('Frame',frame)
      # Press Q on keyboard to  exit
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break

      # Break the loop
      else: 
        break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
    rospy.loginfo("completed video")

  
if __name__ == '__main__':
  try:
    tour()
    rospy.spin()
  except rospy.ROSInterruptException:
    pass 
