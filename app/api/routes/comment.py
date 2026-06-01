from app.schemas.comment import CommentCreate , CommentResponse , CommentUpdate
from app.api.dependencies.post import get_post_by_id
from app.api.dependencies.auth import get_current_user
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.models.comment import Comment
from app.api.dependencies.comment import get_comment_by_id
from fastapi import APIRouter , Depends

from fastapi.exceptions import HTTPException

router = APIRouter()



@router.post('/comments' , response_model=CommentResponse)
def create_comment(
    new_comment : CommentCreate,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    current_post = get_post_by_id(new_comment.post_id , db = db)
    
    comment = Comment(
        content = new_comment.content,
        post_id = current_post.id,
        user_id = current_user.id
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


@router.get('/posts/{post_id}/comments' , response_model=list[CommentResponse])
def get_all_comments_by_post(
    post_id : int,
    db : Session = Depends(get_db)
):
    current_post = get_post_by_id(id=post_id , db = db)
    
    comments = db.query(Comment).filter(
        Comment.post_id == current_post.id
    ).all()

    return comments



@router.put('/comments/{comment_id}' , response_model=CommentResponse)
def update_comment(
    comment_id : int,
    updated_comment : CommentUpdate,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user),
):
    current_comment = get_comment_by_id(comment_id , db)

    if current_comment.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail='you cannot edit another user\'s comment'
        )

    current_comment.content = updated_comment.content
    db.commit()
    db.refresh(current_comment)


    return current_comment



@router.delete('/comments/{comment_id}')
def delete_comment_by_id(
    comment_id : int,
    db : Session = Depends(get_db),
    current_user :User = Depends(get_current_user)
):
    current_comment = get_comment_by_id(comment_id ,db)

    if current_user.id != current_comment.user_id:
        raise HTTPException(
            status_code=403,
            detail='you cannot Delete another users Comment.'
        )
    
    db.delete(current_comment)
    db.commit()

    return {
        'message' : 'Comment deleted successfully'
    }




