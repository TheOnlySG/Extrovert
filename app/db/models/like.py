from sqlalchemy.orm import relationship
from sqlalchemy import DateTime,Integer , Column , String , ForeignKey
from app.db.database import Base
from datetime import datetime , timezone


class Like(Base):

    __tablename__ = 'likes'

    id = Column(Integer , primary_key=True , nullable=False , autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )
    post_id = Column(
        Integer,
        ForeignKey('posts.id'),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc)
    )

    post = relationship(
        'Post',
        back_populates='likes'
    )

    user = relationship(
        'User',
        back_populates='likes'
    )