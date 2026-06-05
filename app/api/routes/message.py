from app.db.database import get_db
from app.schemas.message import MessageCreate , MessageResponse
from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.api.dependencies.user import get_user_by_id
from app.api.dependencies.auth import get_current_user

from app.db.models.user import User
from app.db.models.message import Message

from fastapi.exceptions import HTTPException    

from sqlalchemy import or_ , and_
router = APIRouter()

#this route is mostly not used now , as websocket is implemented. but instead of removing it , i prefered keeping it here.
@router.post('/messages' , response_model=MessageResponse)
def send_message(
    new_message : MessageCreate,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    receiver = get_user_by_id(new_message.receiver_id , db)

    if receiver.id == current_user.id:
        raise HTTPException(
            status_code=400,
            detail='you cant text yourself'
        )
    
    message = Message(
        sender_id = current_user.id,
        receiver_id = receiver.id,
        content = new_message.content
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message


#this is usefull , the route is stil valid after websockets so ill keep it
@router.get(
    '/messages/{user_id}',
    response_model=list[MessageResponse]
)

def get_messages(
    user_id : int,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    target_user = get_user_by_id(user_id=user_id , db = db)

    messages = db.query(Message).filter(
        or_(
            and_(
                Message.sender_id == current_user.id,  
                Message.receiver_id == target_user.id
                ),
            and_(
                Message.receiver_id == current_user.id ,
                Message.sender_id == target_user.id 
                )
        )
    ).order_by(Message.created_at).all()

    return messages