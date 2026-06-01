from app.db.database import Base
from sqlalchemy import Column , String , Integer , DateTime , ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime , timezone


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer , primary_key=True ,nullable=False , autoincrement=True )
    content = Column(String , nullable=False)
    created_at = Column(DateTime(timezone=True) , default=lambda:datetime.now(timezone.utc))

    user_id = Column(
        Integer,
        ForeignKey('users.id')
    )

    post_id = Column(
        Integer,
        ForeignKey('posts.id')
    )

    author = relationship(
        'User',
        back_populates='comments'
    )

    post = relationship(
        'Post',
        back_populates='comments'
    )