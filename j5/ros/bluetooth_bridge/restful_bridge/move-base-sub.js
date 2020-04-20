
const rosnodejs = require('rosnodejs')
const EventEmitter = require('events');

class RosEmitter extends EventEmitter {}

const cmd_velmsgEmitter = new RosEmitter();

function moveCmdCB(msg){
  console.log("move is",msg)
  cmd_velmsgEmitter.emit('update',{
    msg: msg
 });
}

rosnodejs.initNode('data_bridge').then((nh) => {
  nh.subscribe('/cmd_vel','geometry_msgs/Twist',moveCmdCB)
});

//console.log("Test if this runs...");

module.exports = {
  'cmd_velMsg': cmd_velmsgEmitter,

}


