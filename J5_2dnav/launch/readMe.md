#ReadMe and commands
##introduction
  This is the set of files that run the ros navigation stack 
##comands
  first launch the robot configuration launch file. 
  this tells ros what the robot is configured as. it contains the launc for the laser scanner, the camera and the Tf tree. 
###running the mapping applications
  the mapping is to teach the robot the lay of the land and define the points of intrest for the tour this is extremely important for slam as it lets the robot plan routes 
  todo

###running the navigation

  in terminal 1:
   ```
     roslaunch J5_2dnav J5_configuration.launch 
   ```
  second launch the move base file. this will start the navigation stack and handles the movement of the base, the map server and the amcl
  in terminal 2:
   ```
     roslaunch J5_2dnav move_base.launch
   ```
