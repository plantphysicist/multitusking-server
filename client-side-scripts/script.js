$(function () {
    var socket = io.connect();

    //sockets
    socket.on('connect', () => {
        console.log('connected: '+socket.connected);
        socket.emit('hello', 'world')
      });

    socket.on('hey', function(msg){
        console.log(msg)
        ctx.font = "30px Arial";
        ctx.fillText(msg['text'], msg['x'], msg['y']);
    });

    function send_command(command){
        socket.emit('command', command)
    }

    //game

    //vars
    var canvas = document.getElementById("game_canvas");
    var ctx = canvas.getContext("2d");

    //functions
    
    //logic
    if(key_code == 87){
        send_command('moveup')
    }
});