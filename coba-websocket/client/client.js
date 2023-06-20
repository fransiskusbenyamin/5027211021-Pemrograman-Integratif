const wsclient = document.getElementById("wsclient");
const ws = new WebSocket("ws://localhost:8000");

ws.onopen = () => {
    wsclient.innerHTML += "Connected to local websocket Server<br>";
};