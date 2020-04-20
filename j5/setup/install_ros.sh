#!/bin/bash
## Ros version melodic

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
sudo apt update && \
sudo apt install -y ros-melodic-ros-base && \
sudo apt install -y ros-melodic-tf ros-melodic-rplidar-ros git nodejs \
    ros-melodic-cv-bridge ros-melodic-ddynamic-reconfigure \
    ros-melodic-image-transport ros-melodic-diagnostic-updater && \
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc && \
source ~/.bashrc

# set up catkin ws
mkdir -p ~/catkin_ws/src && \
cd ~/catkin_ws && \
catkin_make && \
echo "source /home/$USER/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
echo "alias refresh='source ~/.bashrc'" >> ~/.bash_aliases && \
echo "alias cm='catkin_make -C ~/catkin_ws -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release'" >> ~/.bash_aliases && \
source ~/.bashrc

