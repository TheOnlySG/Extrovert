from pydantic import BaseModel


class LikeResponse(BaseModel):
    model_config = {
        'from_attributes':True
    }

    liked : bool
    likes_count : int