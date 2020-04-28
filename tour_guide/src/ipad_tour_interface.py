######
#this file is for selecting tours

import json
import rospy
import re


class interface:

  def __init__(self):
  #read in all points in  building
  #read in tour locations
  #
  def read_points(self,filename):
  #read in all possible points from json and return dictionary with all possible points
      with open(filename,'r') as l:
      locations= json.load(l)
      rospy.loginfo(locations)
    #read in location list
    #l = '{"origin":{"x": 0.0,"y":0.0,"rz":0.0},"loc1":{"x": 1.0,"y":2.0,"rz":3.0}}'
    #locations= json.loads(l)
    return locations

  def read_tour(self):
  #read the list of points from ipad  

  def calc_cost(self,point1, point2):
  #calc the cost to move from one point to another
  
  def path_optimizer(self):
  # take list and find nearest points
  # loop through locations find nearest 2 points (x dir and y dir)
  # go to point with lowest cost
  

  def save_tour(self):
  #save the newly created tour



def main():


main
  

