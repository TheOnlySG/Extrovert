from fastapi.security import (HTTPBearer , HTTPAuthorizationCredentials)
from fastapi import Depends
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.core.security import verify_access_token
from app.db.models.user import User
from fastapi.exceptions import HTTPException

security = HTTPBearer()

def get_current_user(credentials : HTTPAuthorizationCredentials = Depends(security) , db : Session = Depends(get_db)):

    user_id = verify_access_token(token = credentials.credentials)
    
    current_user = db.query(User).filter(
        User.id == user_id
    ).first()
    
    if current_user is None:
        raise HTTPException(status_code=401 , detail='User Not Found')

    return current_user



