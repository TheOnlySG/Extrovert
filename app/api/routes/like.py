from fastapi import APIRouter , Depends
from app.db.models.user import User
from app.schemas.like import LikeResponse
from app.db.database import get_db
from app.api.dependencies.auth import get_current_user
from sqlalchemy.orm import Session
from app.api.dependencies.post import get_post_by_id
from app.db.models.like import Like
from fastapi.exceptions import HTTPException

router = APIRouter()


@router.post('/posts/{post_id}/likes' , response_model=LikeResponse)
def toggle_like(
    post_id : int,
    db :Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    current_post = get_post_by_id(post_id , db)
    
    existing_like = db.query(Like).filter(
        Like.user_id == current_user.id,
        Like.post_id == post_id
    ).first()

    if existing_like:
        db.delete(existing_like)
        db.commit()
        liked = False
    else:
        new_like = Like(
            user_id = current_user.id,
            post_id = current_post.id
        )
        db.add(new_like)
        db.commit()

        liked = True
    
    likes_count = db.query(Like).filter(
        Like.post_id == current_post.id
    ).count()

    return {
        'liked' : liked,
        'likes_count' : likes_count
    }
