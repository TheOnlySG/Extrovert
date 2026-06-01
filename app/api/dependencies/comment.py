from fastapi import Depends
from app.db.database import get_db
from app.db.models.comment import Comment
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session


def get_comment_by_id(
        comment_id : int,
        db : Session
):
    current_comment = db.query(Comment).filter(
        Comment.id == comment_id
    ).first()

    if not current_comment:
        raise HTTPException(
            status_code=404,
            detail='Comment Not Found'
        )
    return current_comment