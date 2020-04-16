#! /usr/bin/env python

#this is the client for controling a robot with a list of points

#import the required libraries
import rospy
import actionlib
import json
import cv2
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from door.srv import *

#define tour class that contains tour operations
class tour():
 
  def read_locations(self,filename):
  #read in the tour file that contains tour information
    with open(filename,'r') as l:
      locations= json.load(l)
      rospy.loginfo(locations)
    #read in location list
    #l = '{"origin":{"x": 0.0,"y":0.0,"rz":0.0},"loc1":{"x": 1.0,"y":2.0,"rz":3.0}}'
    #locations= json.loads(l)
    return locations


  def __init__(self):
    #start the ros tour node
    argv= rospy.myargv(argv=sys.argv)
    #read file location from command line
    fname = argv[1]
    locations = self.read_locations(fname)
    #begin the tour node
    rospy.init_node('tour',anonymous = False)
    
    for i in locations:
      rospy.loginfo("moving to %s",i.get("name"))
      self.goalReached = self.moveToGoal(i.get("x"), i.get("y"),i.get("rz"))
      if int(i.get("door")) != 0:
        print(type(i.get("door")))
        rospy.loginfo("opening door")
        self.dooropened = self.open_door(int(i.get("door")))
      else:
        rospy.loginfo('no door to open')

  def shutdown(self):
    #stop the program at the end of tour
    rospy.loginfo("quit program")
    rospy.sleep()
  
  def moveToGoal(self,x,y,rz):
    #define a client to send movement commands to the movebase server 
    ac =actionlib.SimpleActionClient("move_base", MoveBaseAction)
    #wait for move base server to come up
    while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
      rospy.loginfo("waiting for move base server")
    #construct move base goal object
    goal = MoveBaseGoal()
    
    #populate data for moving the goal with provided data
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    
    goal.target_pose.pose.position = Point(x,y,0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = rz
    goal.target_pose.pose.orientation.w = 1.0
    #log robot is sending data  and  send goal
    rospy.loginfo("Sending goal location")
    ac.send_goal(goal)
    
    #wait 120 seconds to reach goal
    ac.wait_for_result(rospy.Duration(120))
    
    #check if we made it to the goal 
    if(ac.get_state()== GoalStatus.SUCCEEDED):
      rospy.loginfo("reached goal")
      return True
    else:
      rospy.loginfo("the robot failed to reach the goal")
      return False

  def open_door(self,door):
    rospy.wait_for_service('door')
    rospy.loginfo('opening door number: %s',door)
    od = rospy.ServiceProxy('door', opendoor)
    resp1 = od(door)
    return resp1.opened

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
