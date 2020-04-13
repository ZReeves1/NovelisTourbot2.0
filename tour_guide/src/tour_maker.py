#! /usr/bin/env python

'''
this is the applet for making tour.json files
it uses the 2dnavgoal tool in rviz to mark a pose on the map that the robot uses to navigate.
usage:
	1. open the file that will be the tour.json
	2. mark the first point and press y to confirm or n to select again
  	3. input the location of the video that needs to be played
	4. repeat step 2 and 3 to define all points on tour
	5. save the tour 
	6. close the program
'''
import rospy
import actionlib
import json
import argparse
import sys
from geometry_msgs.msg import Pose, PoseStamped, PoseArray, Quaternion 
from std_msgs.msg import String


class tour_maker:
  locations = []
  def open_tour(self,filename):
    try:
      tour = open(filename,'x')
      rospy.loginfo('created %s',filename)
    except:
      tour = open(filename,'a')
      rospy.loginfo('openned %s for append',filename)
    self.display_poses(tour)

  def push_location(self,lst,datadict):
    lst.append(datadict)
    self.display_poses(lst)    

  
  def __init__(self):
    #self.open_tour_file()
    myargv= rospy.myargv(argv=sys.argv)
    
    #rate = rospy.rate(10)
    rospy.init_node('tour_maker',anonymous= False)
    self.pub = rospy.Publisher('/tour_list',PoseArray,queue_size=10)
    self.open_tour(myargv[1])
    rospy.Subscriber('/move_base_simple/goal',PoseStamped,self.callback)
    
    

  def callback(self,data):
    resp = 'r'
    while (resp != 'n' or resp != 's' ):
      rospy.loginfo('recieved:\n %s\nIs this the correct locataion and pose?(y/n)',data.pose)
      resp = input()
      rospy.loginfo(resp)
      if resp == 'y':
        print('input name for location')
        loc_name = input()
        loc_pose = dict(x = data.pose.position.x, y= data.pose.position.y,rz = data.pose.orientation.z)
        loc =dict(name=loc_name,pose=loc_pose)
        self.push_location(self.locations,loc)
        rospy.loginfo('adding %s to list',loc_name)  
      elif resp == 'n':
        rospy.loginfo('pick again')
      else:
        rospy.loginfo('y or n')
        #rospy.loginfo(type(data.pose.position.x))
      rospy.loginfo('select another location in Rviz, s to save or ctrl-C to quit')
      resp = input()

  def display_poses(self,locs):
    disp = PoseArray()
    disp.header.seq =1
    disp.header.stamp = rospy.Time.now()
    disp.header.frame_id ="map"

    disp.poses = locs
    self.pub.publish(disp)
     
  def save_tour(self,savefile, locs):
    rospy.loginfo('saving %s',savefile)
    savefile.write(json.dumps(locs))

def main():

  try:
    tour_maker()
    rospy.spin()
  except rospy.ROSInterruptException:
    pass 

main()
