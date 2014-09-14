window.onload = function() {
    window.WebSocket = window.WebSocket || window.MozWebSocket || false;

    if(window.WebSocket){
        var chat_area = document.getElementById("chat_area"),
            message_text = document.getElementById("message_text"),
            send_but = document.getElementById("send_message");

        var nickname = document.getElementById("nickname").innerHTML;

        var ws =new WebSocket("ws://"+location.host+"/now");

        var room = "main"

        ws.onopen = function(e) {
            var s = JSON.stringify({
                "new_user": nickname,
                "room": room
            });
            ws.send(s)
            console.log(s)
        }
        ws.onmessage=function(e) {
            data = JSON.parse(e.data);
            if(data.update) {
                var people = data.online;
                var people_list = document.getElementById("users");
                people_list.innerHTML = "";
                for(var i = 0; i < people.length; i++) {
                    var li = document.createElement("li");
                    li.appendChild(document.createTextNode(people[i]));
                    people_list.appendChild(li);
                }
            } else {
                writeMessage(data.message)
            }
        }
        ws.onclose=function(){
            ws.close();
            writeMessage("Disconnected.");
        }

        window.onbeforeunload = function() {
            ws.send_message("/disconnect:" + nickname);
        }

        send_but.onclick = function() {
            sendMessage();
        }

        message_text.onkeydown = function(event) {
            if(event.keyCode == "13") {
                sendMessage();
            }
        }

        function sendMessage() {
            var message = message_text.value;
            if(message) {
                message = nickname + ": " + message;
                var s = JSON.stringify({
                    "message": message,
                    "room": room
                });
                ws.send(s);
                message_text.value = "";
            }
        }

        function writeMessage(msg) {
            chat_area.value += msg + "\n";
            chat_area.scrollTop = chat_area.scrollHeight;
        }
    } else {
        alert("No WebSocket Support");
    }
}