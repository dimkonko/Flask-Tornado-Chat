import json
import redis
from tornado.websocket import WebSocketHandler

class User(object):
    def __init__(self, name, room, connection):
        self.name = name
        self.room = room
        self.connection = connection

    def write_message(self, msg):
        self.connection.write_message(msg)


class Room(object):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.users = list()

    def add_user(self, user):
        self.users.append(user)

    def broadcast(self, msg):
        for user in self.users:
            user.write_message(msg)


class NowHandler(WebSocketHandler):
    #comand_tag = "/"
    clients = list()
    rooms = list()

    rooms.append(Room("main", "Admin"))
    
    @staticmethod
    def broadcast(user_room, msg):
        for room in NowHandler.rooms:
            if room.name == user_room:
                room.broadcast(msg)
    
    def open(self):
        NowHandler.clients.append(self)
        print "Connected"

    def on_message(self, message):
        print message
        message_dict = json.loads(message)

        if "new_user" in message_dict:
            """Register new user"""
            user = User(message_dict["new_user"], message_dict["room"],
                        NowHandler.clients[-1])
            self.get_room_by_name(message_dict["room"]).add_user(user)
        elif "new_room" in message_dict:
            """Register new room"""
            room = Room(message_dict["new_room"], message_dict["owner"])
            NowHandler.rooms.append(room)
        else:
            NowHandler.broadcast(
                message_dict["room"],
                {"message": message_dict["message"]}
            )
        # if message[0] == NowHandler.comand_tag:
        #     data = message.split(':')
        #     if data[0] == "/nickname":
        #         NowHandler.users.append(data[1])

        #     NowHandler.broadcast({
        #         "online": NowHandler.users,
        #         "update": True
        #     })
        # else:
    	   # NowHandler.broadcast({"message": message})
        #print NowHandler.users
    
    def on_close(self):
        counter = 0
        for item in NowHandler.clients:
            if item == self:
                print "Closed for :"
                print NowHandler.users[counter]
                del NowHandler.users[counter]
            counter += 1
        NowHandler.clients.remove(self)

    def get_room_by_name(self, room_name):
        for room in NowHandler.rooms:
            if room.name == room_name:
                return room
