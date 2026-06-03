from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from app.db.models.user import User


def get_user_by_id(
        user_id : int,
        db : Session
):
    
    received_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not received_user:
        raise HTTPException(
            status_code=404,
            detail='user not found'
        )
    
    return received_user