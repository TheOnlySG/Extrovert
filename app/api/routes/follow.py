from app.schemas.follow import FollowResponse
from app.db.models.follow import Follow
from app.db.models.user import User
from app.api.dependencies.auth import get_current_user
from fastapi import APIRouter
from app.db.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.exceptions import HTTPException

router = APIRouter()

@router.post('/users/{user_id}/follow' , response_model=FollowResponse)
def toggle_follow(
    user_id  : int,
    db : Session = Depends(get_db),
    current_user  : User = Depends(get_current_user)
):
    if current_user.id == user_id:
        raise HTTPException(
            status_code=400,
            detail="you cannot follow yourself"
        )
    searching_for_follower = db.query(User).filter(
        User.id == user_id
    ).first()

    if not searching_for_follower:
        raise HTTPException(
            status_code=404,
            detail='user not found'
        )
    check_follow = db.query(Follow).filter(
        searching_for_follower.id == Follow.following_id,
        current_user.id == Follow.follower_id
    ).first()

    if check_follow:
        db.delete(check_follow)
        db.commit()
        return {
            'following' : False,
            'followers_count' : current_user.followers_count,
            'following_count' : current_user.following_count
        }

    new_follow = Follow(
        follower_id = current_user.id,
        following_id = user_id
    )   
    db.add(new_follow)
    db.commit()
    db.refresh(new_follow)

    return {
        'following' : True,
        'followers_count' : current_user.followers_count,
        'following_count' : current_user.following_count
    }