const express = require('express');
const http = require('http');
const app = express();
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
    console.log("User connected")

    socket.on('chat message', (msg) => {
        io.emit('chat message', msg)
    });

    socket.on('disconnect', () => {
        console.log("User disconnected")
    });
});

server.listen(8000, () => {
    console.log("listening on *:8000")
});