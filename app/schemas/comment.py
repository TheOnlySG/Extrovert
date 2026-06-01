from pydantic import BaseModel
from datetime import datetime
from app.schemas.user import UserMini

class CommentCreate(BaseModel):
    content : str
    post_id : int


class CommentResponse(BaseModel):

    model_config = {
        'from_attributes' : True
    }

    id : int
    content : str
    created_at : datetime
    author : UserMini

class CommentUpdate(BaseModel):
    model_config = {
        'from_attributes' : True
    }

    content : str