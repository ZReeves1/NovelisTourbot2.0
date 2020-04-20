const rosnodejs = require('rosnodejs')
const EventEmitter = require('events');

class LidarEmitter extends EventEmitter {}

const lidarMsgEmitter = new LidarEmitter();


function lidarCB(msg){
  console.log("scan is", msg.ranges.length, "points long.")
  lidarMsgEmitter.emit('update', {
    ranges: msg.ranges,
    angle_min: msg.angle_min,
    angle_max: msg.angle_max
  })
}

rosnodejs.initNode('bt_bridge').then((nh) => {
  nh.subscribe('/scan', 'sensor_msgs/LaserScan', lidarCB)
});

console.log("Test if this runs...");

module.exports = {
  'lidarMsg' : lidarMsgEmitter
}
// lidarMsg.on('update', (msg)=>{global_msg = msg});
