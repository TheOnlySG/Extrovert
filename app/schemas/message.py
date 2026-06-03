from pydantic import BaseModel
from datetime import datetime


class MessageResponse(BaseModel):
    
    model_config={
        'from_attributes' : True
    }
    
    id  :int
    sender_id : int
    receiver_id : int
    content : str
    created_at :datetime

class MessageCreate(BaseModel):
    receiver_id : int
    content : str