from pydantic import BaseModel
from datetime import datetime

from app.schemas.user import UserMini

class PostCreate(BaseModel):
    content  : str #as while creating , user will ofc only send content


class PostResponse(BaseModel):

    model_config = {
        'from_attributes' : True
    } #this will allow return post in route as post is an orm object


    id : int
    content : str
    created_at : datetime
    author : UserMini