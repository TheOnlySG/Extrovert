from pydantic import BaseModel



class FollowResponse(BaseModel):
    model_config = {
        'from_attributes':True
    }

    following : bool
    followers_count : int
    following_count : int