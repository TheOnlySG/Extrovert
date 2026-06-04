from app.db.database import get_db
from app.db.models.user import User
from app.db.models.post import Post

from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.dependencies.auth import get_current_user

from app.schemas.post import PostResponse

from fastapi import APIRouter

router = APIRouter()


@router.get('/feed' , response_model=list[PostResponse])
def get_feed_by_following(
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    following_ids = [
        follow.following_id for follow in current_user.following
    ] #mhanje get all users whome the current user follows
    '''
    here we might have done an orm query with in_ , but no need as we already had relationships
    which are as follows :
    user.following will return all the users whome the current user follows , its a property we wrote
    so we are simply fetching only ids from it and making a list
    '''

    if not following_ids:
        return [] #if no following return empty list
    
    
    posts = db.query(Post).filter(
        Post.user_id.in_(following_ids)
    ).order_by(Post.created_at.desc()).all()
    #get all posts by ppl who are in following_ids , and sort them by created_at in descending

    return posts
