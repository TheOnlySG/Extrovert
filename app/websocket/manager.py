from fastapi import WebSocket
# from app.db.models.message import Message

#lets build the connection manager in this file
'''
so it will basically store a hashmap which has userid : connected something like this
to mark which users are connected , which are disconnected , and thus avoiding pooling for all users
and buring resources
'''


class ConnectionManager:
    

    def __init__(self):
        self.active_connections = {}
    
    async def connect(
            self ,
            user_id : int,
            websocket : WebSocket
    ):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(
            self , 
            user_id : int,
    ):
        self.active_connections.pop(user_id , None)

    async def send_json(
            self , 
            receiver_id : int,
            payload : dict
    ):
        receiver_socket = self.active_connections.get(receiver_id)
        if receiver_socket:
            await receiver_socket.send_json(
                payload
            )


'''
now , if we create a new COnnectionManager object everytime in route , it will create many active_connections
and the whole purpose of it would get killed ,

so we need 1 centralized object which we will use in order to maintain a single hashmap of
active connections.
thus :
'''


manager = ConnectionManager()

'''
we will import this everywhere
'''


