# J5 Ros navigation stack read me
## introduction
This is the j5 ros package it contains the launch files and required packages for the ros package. simulation is based on the turtle bot from the ros tutorials "http://wiki.ros.org/navigation/Tutorials"
the main feature is the tour guide module that contains the code to run a tour. my goal for this project is to make it clear enough for someone to easily understand what has been done on the project and pick up where I have left off.
## requirements
ros-melodic 
ros navigation stack https://wiki.ros.org/navigation
ros-keyboard teleop
simulation requires:
ros turtlebot packages
ros gazebo
real robot requires
intel realsense drivers
slamtec lidar package
double 2 robot with ipad
## contents
the directories contain the following packages
tour_guide
door
various other packages for testing purposes 
# usage
## tour structure
this navigation implemetaon relies on pre mapping the building that will be toured and providing a list of points for the robot to take people to see. tours need to also have doors  listed as points of intrest and thier ids listed as points of intrest 
```javascript
[{"name":"name of location",
	 "x": x corrdnate,
	 "y":y cooridnate,
	 "rz":rotation about the z axis,
         "video":"video location",
         "door":"door id, 0 if there is no door"}]
```

## real robot

### mapping

### navigation and tourguide mode

## simulation
the simulation was built of the turtlebot tutorials do to the rapid on set of corona virus and rapidly aproaching end of the semester.
#### launch gazebo
first we launch gazebo, the simulator for ros. in this case we use the house world as it is complex just like the novelis building and is a good test for the logic used to control the robot
```
export TURTLEBOT3_MODEL=waffle
roslaunch turtlebot3_gazebo turtlebot3_house.launch
```
#### mapping
```
export TURTLEBOT3_MODEL=waffle
roslaunch turtlebot3_slam turtlebot3_slam.launch
```
#### Remote key board control
```
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
### navigation/tourguide mode
#### terminal 1 --launch gazebo with house 
```
export TURTLEBOT3_MODEL=waffle
roslaunch turtlebot3_gazebo turtlebot3_house.launch
```
#### terminal 2
```
export TURTLEBOT3_MODEL=waffle
roslaunch turtlebot3_navigation turtlebot3_navigation.launch
```
this lau
#### terminal 3
```
roslaunch tour_guide tour_guide.launch
```
## trouble shooting tips
| problem                          	| cause                                                     	| solution                                                                             	|
|----------------------------------	|-----------------------------------------------------------	|--------------------------------------------------------------------------------------	|
| robot cannot create path to goal 	| something is in the way<br>there is something on the goal 	| remove object that is in the way<br>makes sure there are no artifacts from the start 	|
