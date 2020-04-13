# J5 Ros navigation stack read me
## introduction
This is the j5s ros package it contains the launch files and required packages for the ros package. simulation is based on the turtle bot from the ros tutorials "http://wiki.ros.org/navigation/Tutorials"
## requirements
ros-melodic 
simulation requires gazebo

# usage
## real robot
### mapping
### navigation and tourguide mode

## simulation
### mapping
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
```
### navigation/tourguide mode
#### terminal 1
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_gazebo turtlebot3_house.launch
```
#### terminal 2
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/house_map.yaml
```
#### terminal 3
```
$ export TURTLEBOT3_MODEL=waffle
$ rosrun rviz rviz -d `rospack find turtlebot3_navigation`/rviz/turtlebot3_nav.rviz
```
