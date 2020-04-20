var bleno = require('bleno');

console.log("Hello!");
 
var LidarCharacteristic = require('./lidar-bt-characteristic');

function stop(){
  console.log("stopping!")
  bleno.stopAdvertising(function(error){console.log("stopped advertising")});
  process.exit()
}

bleno.on('stateChange', function(state) {
  console.log('on -> stateChange: ' + state);

  if (state === 'poweredOn') {
    var name = 'j5-sensors';
    var serviceUuids = ['5CA4'];
    bleno.startAdvertising(name, serviceUuids);
    //setTimeout(stop, 60*1000)
  } else {
    stop()
  }
});


bleno.on('advertisingStart', function(error) {
  console.log('on -> advertisingStart: ' + (error ? 'error ' + error : 'success'));

  if (!error) {
    bleno.setServices([
      new bleno.PrimaryService({
        uuid: '5CA4',
        characteristics: [
          new LidarCharacteristic()
        ]
      })
    ]);
  }
});


process.on('SIGINT', function() {
    console.log("Caught interrupt signal");
    stop()
    if (i_should_exit)
        process.exit();
});


