from app.db.database import Base
from sqlalchemy import Integer , String , Column ,DateTime , ForeignKey 
from sqlalchemy.orm import relationship
from datetime import datetime , timezone



class Post(Base):
    
    __tablename__ = 'posts'
    
    id = Column(Integer , autoincrement=True , nullable=False , primary_key=True)
    content = Column(String , nullable=False)
    created_at = Column(
        DateTime(timezone=True) ,
        default=lambda:datetime.now(timezone.utc)
    )
    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )

    author  =relationship(
        'User',
        back_populates='posts'
    )