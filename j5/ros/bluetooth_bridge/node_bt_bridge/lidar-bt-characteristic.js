var util = require('util');
var bleno = require('bleno');
var rosEmitter = require('./lidar-ros-subscriber')

var LidarCharacteristic = function() {
  LidarCharacteristic.super_.call(this, {
    uuid: '0000',
    properties: ['read', 'write', 'notify'],
    //value: null
  });

  this._value = new Buffer(0);
  this._updateValueCallback = null;
  this.lidarEmitter = rosEmitter.lidarMsg
  this.lidarEmitter.on('update', (lidar_data) => {
    var n_transmit = 8
    var ranges_transmit = []
    var ranges_orig = Array(lidar_data.ranges)[0]

    // var maxval = 0
    // var minval = 1
    // for (var i=0;i<ranges_orig.length;i+=1){
    //   if (ranges_orig[i] < minval){
    //     minval = ranges_orig[i];
    //   }
    //   if (ranges_orig[i] > maxval) {
    //     maxval = ranges_orig[i];
    //   }
    // }
    // console.log('min', minval, 'max', maxval)

    ranges_orig = ranges_orig.map((x)=>{
      if (isFinite(x)){
        return x
      } else {
        return 0
      }
    });

    var n_orig = ranges_orig.length
    if (n_orig < 1){
      return;
    }
    if (n_transmit > n_orig) {
      return
    }

    var zero_counts = []
    var transmit_idx = 0
    for (var i=0;i<n_orig;i+=1){
      //console.log(i*(n_transmit)/(n_orig), " --floor--> ", Math.floor(i*(n_transmit)/(n_orig)))
      transmit_idx = Math.floor(i*(n_transmit)/(n_orig))
      if (ranges_transmit.length < (transmit_idx + 1)) {
        ranges_transmit.push(10.2)
        zero_counts.push(0)
      }
      // minpool ignoring invalid reading zero number
      if (ranges_orig[i] > 0 && ranges_orig[i] < ranges_transmit[transmit_idx] && ranges_transmit[transmit_idx] != 0){
        ranges_transmit[transmit_idx] = ranges_orig[i]
      }
      else {
        // if over 50% invalid, record a zero.
        if (ranges_orig[i] == 0) {
          zero_counts[transmit_idx] += 1
          if (zero_counts[transmit_idx] > 0.7 * n_orig / n_transmit){
            ranges_transmit[transmit_idx] = 0
          }
        }
      }
      //console.log(i, ranges_orig[idx_approx])
    }
    //console.log(ranges_transmit)
    var ranges_transmit_2cm = ranges_transmit.map((x)=>{
      // x_m * 100_cm/m * (1_2cm / 2_cm) = x_2cm
      // each one int is 2 cm (compressed 2cm resolution with max range of 5m)
      var cm_2 = Math.round(x*50)
      if (cm_2 < 2){ // set really close to 0
        cm_2 = 0
      }
      if (cm_2 > 256){ // set out of range to 1
        cm_2 = 1
      }
      return cm_2
    })
    console.log(ranges_transmit_2cm)
    //console.log(ranges_transmit_2cm)
    this._value = Buffer.from(ranges_transmit_2cm)
    if (this._updateValueCallback) {
      console.log('LidarCharacteristic - onWriteRequest: notifying');
      this._updateValueCallback(this._value);
    }
  })
};

util.inherits(LidarCharacteristic, bleno.Characteristic);

LidarCharacteristic.prototype.onReadRequest = function(offset, callback) {
  console.log('LidarCharacteristic - onReadRequest: value = ' + this._value.toString('hex'));

  callback(this.RESULT_SUCCESS, this._value);
};

LidarCharacteristic.prototype.onWriteRequest = function(data, offset, withoutResponse, callback) {
  //this._value = data;

  console.log('LidarCharacteristic - onWriteRequest: value = ' + this._value.toString('hex'));

  // if (this._updateValueCallback) {
  //   console.log('LidarCharacteristic - onWriteRequest: notifying');

  //   this._updateValueCallback(this._value);
  // }

  callback(this.RESULT_SUCCESS);
};

LidarCharacteristic.prototype.onSubscribe = function(maxValueSize, updateValueCallback) {
  console.log('EchoCharacteristic - onSubscribe');

  this._updateValueCallback = updateValueCallback;
};

LidarCharacteristic.prototype.onUnsubscribe = function() {
  console.log('EchoCharacteristic - onUnsubscribe');

  this._updateValueCallback = null;
};

module.exports = LidarCharacteristic;
