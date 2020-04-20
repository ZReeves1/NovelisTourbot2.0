# J5

Programs and data for the J5 Robotics Platform

License: GPLv3

Authors: Alec Graves, Sean Owens, and Kevin Martinez

*Created for our 2019 KSU Mechatronics Capstone Project*

## What is this?

The J5 Robotics Platform is an extension of the Double 2 robotic platform with
a myriad of tools for interfacing with external sensors. Due to the J5 platform using 
ROS communication library, the possibilities are truly endless.


## How does this work?

The Double 2 platform contains tools for robotic control from an IOS device.
J5 extends these tools to add support for data transfer from a linux Single Board Computer (SBC) and the ROS library to the IOS control device.
Additionally, we add SWIFT support to the original SDK, thereby improving accessability to higher-level control.

Here are some of the components we use in the J5 Platform:
- Double 2 Robot
- 9.5" iPad Pro and iPad 6th Gen.
- LattePanda 4G/64GB
- RPLidar A1M8


## Directory Structure

- `setup/` containes multiple scripts for configuring the On-Board Sensor Computer
- `ros/` contains catkin programs which are used to gather and process using ROS
- `ios/` (`TODO`) contins IOS programs for the Double 2 Control iPad.


## Choices we made along the way...

#### Main Processing and Control Computer
The platform technically supports control from a web-interface along with control from an IOS SDK. Controlling the Double 2 platform through the IOS SDK was chosen over the web interface for the following reasons:
- The iPad already fulfills the objective of displaying tour videos to users.
- The IOS SDK was determined to be more stable with an interface to controlling the Double 2 platform.
- Using the web-interface would require additional network configuration for each location J5 is used and could limit access to external networks while the computer is connected to the platform.
- The IOS SDK is more developed and allows access to greater control functionality.

#### Connection to External Sensors
Another choice faced was the choice of connection between the iPad and external sensors such as Lidar and RFID Tag reader. These devices are relatively simple and require only a serial connection for data transfer. One problem faced with connecting these devices directly to the iPad is IOS makes it difficult to interface with physical hardware over a simple serial connection, requiring special registration and licensing from Apple, Inc. It was deemed that some other on-platform computing devices would be needed to read sensor data directly and transmit it to the iPad in the time horizon dictated by this project. It was determined that possibilities within our weight limit for this device included microcontrollers and more powerful SBCs running an Operating System (OS). A more powerful SBC with and OS was chosen because of these reasons:
- It was deemed difficult to create low-level interfaces for processing and transmitting data from multiple sensors on a microcontroller within the time constraints of this project.
- An SBC with an OS would allow for a much simpler addition of new sensors and advanced functionality through the use of supported device drivers, high-level hardware communication ecosystems such as Robot Operating System (ROS), and many software libraries that support such a system.
- Extensibility and ability to expand easily in the future is a key-focus of J5, so the severe restrictions caused by using a microcontroller are unacceptable.
- Even a high-end SBC would consume less than 20% of our overall monetary budget.

#### Data Transfer between SBC and iPad
Another decision was the data transmission interface between the Single Board Computer (SBC) and the iPad. Similarly to the previous decision, the options for transmission were a Wi-Fi-based data transmission system and a Bluetooth Low Energy (BLE) interface. BLE does have a lower overall data transmission speed, but BLE was chosen for these reasons:
- Wi-Fi would require placing additional hardware on J5 (a router) or would require reliance on external wireless hardware outside of our control or would require complex network configuration (Peer-to-Peer) that would complicate connections to other networks such as the internet.
- Wi-Fi could suffer from dead-zones and complete failure due to configuration changes if relying on external networking equipment.

#### Which SBC to Use
One final decision made was the use of the LattePanda 4G/64GB SBC. The LattePanda 4G/64GB was chosen as the on-board computer of choice in the face of multiple seemingly-viable alternatives such as the Raspberry PI, the Odriod XU4, Jetson Nano, and Jetson TX1. All of these computing systems would fall within our budget and several of them offer improved compute capability over the LattePanda for parallelizable tasks such as running Machine Learning (ML) models. The reason these systems are discarded as viable options is their CPU architecture.  Of the mentioned systems, the LattePanda 4G/64GB is the only one that features an x86_64 CPU instruction set. The others feature ARM processors. Many low-cost, high-performance devices that could be used to extend the J5 system in the future such as the Intel RealSense camera module line have no official support for ARM computers. Pair this with the reality of many modern libraries not fully supporting ARM, and the development time lost to having to work around ARM support limitations could cause the project to fail completely. Additionally, having an x86_64 CPU makes the system binary-compatible with the majority of modern development computers. This potentially saves days of troubleshooting compatibility issues between programs created on x86_64 development computers and transferred to ARM computers for the actual J5 system. Finally, the cost of the LattePanda 4G/64GB is still only 20% of our overall budget and significantly less than other x86_64 SBCs such as the LattePanda Alpha or the UDOO BOLT V3.

#### Lidar Sensor
One more decision was the RPLidar vs another sensor. The RPLidar was chosen for the following advantages it had over competitors:
- The RPLidar is offered at a price-point of only $100.
- The RPLidar is available from several major vendors that the Client can easily make purchases from, unlike the similar alternative YDLidar.
- The RPLidar has up-to-date Robot Operating System (ROS) support.

#### Lidar Gimbal
A decision on the Gimbal design was made driven mostly by the weight, even though an active gimbal is more precise and can keep the object in an almost perfect horizontal position, in this particular case it was not required. The robot does not tilt in an angle that would justify the extra cost, weight, and complexity of an electronic gimbal. We first designed the gimbal to take into consideration the main two axes, and it was then decided to only take into consideration one, being the forward axes where the robot does incline; while on the side by side axes it could see a small inclination if it drives on top of a small object such as a cable. By reducing the two axes to just one, opening holes on the side of the support, and implementing a new design with a self-tightening part in order to avoid extra parts such as screws and clamps the weight was lowered to almost 50% of the initial weight. 
