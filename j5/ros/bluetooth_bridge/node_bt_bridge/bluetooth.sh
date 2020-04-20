#!/bin/sh
sudo rfkill unblock all && \
sudo hciconfig hci1 down && \
sudo hciconfig hci1 up && \
sudo -E su -c "export PYTHONPATH=/opt/ros/melodic/lib/python2.7/dist-packages && source /opt/ros/melodic/setup.bash && BLENO_HCI_DEVICE_ID=1 node index.js"
