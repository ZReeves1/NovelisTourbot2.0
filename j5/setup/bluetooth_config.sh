#!/bin/bash
sudo sh -c 'echo "PRETTY_HOSTNAME=j5-sensors" >> /etc/machine-info'
sudo usermod -G bluetooth -a $USER

