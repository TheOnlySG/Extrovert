from fastapi import APIRouter , WebSocket
from app.websocket.manager import manager
from app.db.models.message import Message
from app.db.database import SessionLocal
from fastapi import WebSocketDisconnect
from app.core.security import verify_access_token
from fastapi.exceptions import HTTPException


router = APIRouter()






@router.websocket('/ws')
async def websocket_endpoint(
    websocket:WebSocket,
):
    
    token = websocket.query_params.get('token')
    if not token:
        await websocket.close()
        return
    
    try:
        user_id = verify_access_token(token)
    except HTTPException:
        await websocket.close()
        return


    db = SessionLocal()
    try :

        await manager.connect(user_id=user_id , websocket=websocket) #this will establish connection and
        #maintain a log for us in active responses


        while True:
            data = await websocket.receive_json()

            receiver_id = data['receiver_id']
            content = data['content']

            message = Message(
                sender_id = user_id,
                receiver_id = receiver_id,
                content = content
            )

            db.add(message)
            db.commit()
            db.refresh(message)

            payload = {
                'id' : message.id,
                'sender_id' : message.sender_id,
                'receiver_id' : message.receiver_id,
                'content' : message.content,
                'created_at' : str(message.created_at)
            }

            await manager.send_json(receiver_id=receiver_id , payload=payload)
    except WebSocketDisconnect:
        #thus user with 'user_id' closed browser or say disconnected , we handle it with our function
        manager.disconnect(user_id)
    finally:
        db.close()
