from fastapi import  APIRouter , Depends
from app.db.models.post import Post
from app.schemas.post import PostCreate , PostResponse
from app.api.dependencies.auth import get_current_user
from app.db.models.user import User
from sqlalchemy.orm import Session
from app.db.database import get_db
from fastapi.exceptions import HTTPException
from app.api.dependencies.post import get_post_by_id
router = APIRouter()

@router.post('/posts' , response_model=PostResponse)
def create_post(
    post : PostCreate,
    current_user : User = Depends(get_current_user),
    db : Session = Depends(get_db)
):
    new_post = Post(
        content = post.content,
        user_id = current_user.id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post



@router.get('/posts' , response_model=list[PostResponse]) #as we are going to return all posts , soo we will have a list of post responses
def get_all_posts(
    db : Session = Depends(get_db)
):
    posts = db.query(Post).all()
    return posts


@router.get('/posts/{post_id}' , response_model=PostResponse)
def get_single_post(post_id : int , db : Session = Depends(get_db)):
    return get_post_by_id(post_id , db)


@router.delete('/posts/{post_id}')
def delete_post(post_id : int , db : Session = Depends(get_db) ,
                current_user : User = Depends(get_current_user)):
    
    current_post = get_post_by_id(post_id , db)

    if current_post.user_id != current_user.id :
        raise HTTPException(
            status_code = 403 ,
            detail= "you cannot delete another user's post"
        )
    
    db.delete(current_post)
    db.commit()

    return {
        'message' : 'post deleted successfully'
    }

@router.put('/posts/{post_id}' , response_model=PostResponse)
def update_post(
    post_id : int ,
    updated_post : PostCreate,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
    ):    
    current_post = get_post_by_id(post_id , db)

    if current_post.user_id != current_user.id :
        raise HTTPException(
            status_code=403,
            detail="you cannot update another user's post"
        )
    current_post.content = updated_post.content
    db.commit()
    db.refresh(current_post)
    
    return current_post
