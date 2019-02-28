const WebSocket = require("ws");

const WebSocketServer = WebSocket.Server;

const wss = new WebSocketServer({
    port: 3000
});

wss.on("connection", function (ws) {
    console.log(`new connection:`);
    ws.on("message", function (message) {
        console.log(`recv:${message}`);
        ws.send(`${message}`, (err)=>{
            if(err){
                console.log("error");
            }
        })
    })
});

console.log("hello world");
