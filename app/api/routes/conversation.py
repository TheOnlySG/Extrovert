from app.db.database import get_db
from app.schemas.user import UserMini
from app.db.models.user import User
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from app.api.dependencies.auth import get_current_user

from app.db.models.message import Message

router = APIRouter()


@router.get('/conversations' , response_model=list[UserMini])
def get_conversation(
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    
    sent_messages = db.query(Message).filter(
        Message.sender_id == current_user.id
    ).all()

    received_messages = db.query(Message).filter(
        Message.receiver_id == current_user.id
    ).all()

    #extracting users

    sent_to = [
        msg.receiver_id for msg in sent_messages
    ]

    received_from = [
        msg.sender_id for msg in received_messages
    ]

    partner_ids = list(
        set(sent_to + received_from)
    )

    if not partner_ids : return []

    users = db.query(User).filter(
        User.id.in_(partner_ids)
    ).all()

    return users