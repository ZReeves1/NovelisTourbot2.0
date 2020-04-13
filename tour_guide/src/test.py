import json

def read_locations(filename):
  with open(filename,'r') as l:
    locations= json.load(l)
    #print(locations)
    #read in location list
    #l = '{"origin":{"x": 0.0,"y":0.0,"rz":0.0},"loc1":{"x": 1.0,"y":2.0,"rz":3.0}}'
    #locations= json.loads(l)
  return locations

loc=read_locations('/home/spencer/catkin_ws/src/novelis_senior_design/tour_guide/tours/tour.json')

print(loc[1].get("name"))
