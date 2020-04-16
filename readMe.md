# J5 Ros navigation stack read me
## introduction
This is the j5 ros package it contains the launch files and required packages for the ros package. simulation is based on the turtle bot from the ros tutorials "http://wiki.ros.org/navigation/Tutorials"
the main feature is the tour guide module that contains the code to run and create lists of locatiopns
## requirements
ros-melodic 
ros navigation stack
ros- keyboard teleop
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
##file structure

# usage

## real robot

### mapping

### navigation and tourguide mode

## simulation

#### launch gazebo
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

```

