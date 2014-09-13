from tornado.websocket import WebSocketHandler

class NowHandler(WebSocketHandler):
    comand_tag = "/"
    clients = set()
    people = list()
    
    @staticmethod
    def broadcast(msg):
        for client in NowHandler.clients:
            client.write_message(msg)
    
    def open(self):
        NowHandler.clients.add(self)

    def on_message(self, message):
        if message[0] == NowHandler.comand_tag:
            data = message.split(':')
            if data[0] == "/nickname":
                NowHandler.people.append(data[1])

            NowHandler.broadcast({
                "online": NowHandler.people,
                "update": True
            })
        else:
    	   NowHandler.broadcast({"message": message})
        print NowHandler.people
    
    def on_close(self):
        counter = 0
        for item in NowHandler.clients:
            if item == self:
                print "Closed for :"
                print NowHandler.people[counter]
                del NowHandler.people[counter]
            counter += 1
        NowHandler.clients.remove(self)
