/*
this is where the rosnode.js server gets its data to publish from 
*/

//check for the required packages
const rosnodejs = require('rosnodejs')
const EventEmitter = require('events');

//creates ros emitter class that is a copy of the event emmiter class
class RosEmitter extends EventEmitter {}

//these are the emitter objects that gather ros data and send it to the robot

/*
example:
const emittername = new RosEmitter();
*/
const cmd_velmsgEmitter = new RosEmitter();
//const lidarMsgEmitter = new RosEmitter();
const posMsgEmitter = new RosEmitter();
const roslogMsgEmiter = new RosEmitter();

//these are where we gather data to send to the server using these call backs
/*
example:
//function nameOfFunction(msg to publish){
  emitter.emit('update',{
     msg.data to publish
    });
}
*/

function moveCmdCB(msg){
  console.log("move is",msg.linear)
  cmd_velmsgEmitter.emit('update',{
    cmd: msg
   // az: msg.angular.z
  });
}

function posCB(msg){
  posMsgEmitter.emit('update', {
    msg
  });
}

function roslogCB(msg){
  roslogMsgEmiter.emit('update',{
   msg});
}

//initiate the ros node that executes the callbacks
/*
example:
nh.subscribe('desired ros topic', 'subscribed data type',callback function)
*/
rosnodejs.initNode('data_bridge').then((nh) => {
  nh.subscribe('/amcl_pose', 'geometry_msgs/PoseWithCovarianceStamped', posCB)
  nh.subscribe('/cmd_vel','geometry_msgs/Twist',moveCmdCB)
  nh.subsrcibe('/rosout','String',roslogCB) 
});

console.log("Test if this runs...");

module.exports = {
  'cmd_velMsg': cmd_velmsgEmitter,
  //'lidarMsg' : lidarMsgEmitter,
  'posMsg': posMsgEmitter
}
// lidarMsg.on('update', (msg)=>{global_msg = msg});
