from app.db.database import Base
from sqlalchemy import ForeignKey, Column , Integer , String , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime , timezone

class Message(Base):

    __tablename__ = 'messages'


    id = Column(Integer , autoincrement=True , primary_key=True , nullable=False)
    sender_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )
    receiver_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )
    content = Column(String , nullable=False)

    created_at = Column(DateTime(timezone=True) , default=lambda:datetime.now(timezone.utc))


    sender = relationship(
        'User',
        foreign_keys=[sender_id],
        back_populates='sent_messages'
    )
    
    receiver = relationship(
        'User',
        foreign_keys=[receiver_id],
        back_populates='received_messages'
    )