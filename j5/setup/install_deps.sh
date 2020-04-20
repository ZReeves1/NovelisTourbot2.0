#!/bin/bash

#cd ~/catkin_ws/src && \
#git clone https://github.com/EAIBOT/ydlidar.git --recursive --depth=1
#cm

sudo apt install python-pip bluez-tools bluez libbluetooth-dev && \
#sudo -H python -m pip install pybluez

sudo apt install curl && \
wget https://npmjs.org/install.sh && \
sudo sh install.sh && \
sudo chown -R 1000:1000 "/home/$USER/.npm" && \

sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE && \
sudo add-apt-repository "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo bionic main" -u && \

sudo apt-get install librealsense2-dkms && \
sudo apt-get install librealsense2-utils && \
sudo apt-get install librealsense2-dev && \
sudo apt-get install librealsense2-dbg && \
sudo apt-get install librealsense2 && \
sudo apt-get install libeigen3-dev
