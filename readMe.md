# J5 Ros navigation stack read me
## introduction
This is the j5s ros package it contains the launch files and required packages for the ros package. simulation is based on the turtle bot from the ros tutorials "http://wiki.ros.org/navigation/Tutorials"
the main feature is the tour guide module that contains the code to run and create lists of locatiopns
## requirements
ros-melodic 
simulation requires gazebo
real robot requires

# usage
## real robot
### mapping
### navigation and tourguide mode
## simulation
#### launch gazebo
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_gazebo turtlebot3_house.launch
```
#### mapping
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_slam turtlebot3_slam.launch
```
#### Remote key board control
```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
### navigation/tourguide mode
#### terminal 1 --launch gazebo with house 
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_gazebo turtlebot3_house.launch
```
#### terminal 2
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch
```
#### terminal 3
```
$ export TURTLEBOT3_MODEL=waffle
$ rosrun rviz rviz -d `rospack find turtlebot3_navigation`/rviz/turtlebot3_nav.rviz
```

