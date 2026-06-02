from app.db.database import Base
from sqlalchemy import ForeignKey, Column , Integer ,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime , timezone

class Follow(Base):
    __tablename__ = 'follows'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    follower_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )

    following_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )


    created_at = Column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc)
    )

    follower = relationship(
        'User',
        foreign_keys=[follower_id],
        back_populates='following'
    )
    following = relationship(
        'User',
        foreign_keys=[following_id],
        back_populates='followers'
    )
    