var dgram = require("dgram");

var socket = dgram.createSocket("udp4");
socket.bind(function () {
  socket.setBroadcast(true);
});

var key = event.keyCode;
var message = new Buffer("key");
socket.send(message, 0, message.length, 80, '140.143.72.70', function(err, bytes) {
  socket.close();
});