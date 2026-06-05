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
    image_url = Column(String, nullable=True)
    author  =relationship(
        'User',
        back_populates='posts'
    )

    comments = relationship(
        'Comment',
        back_populates='post'
    )

    likes = relationship(
        'Like',
        back_populates='post'
    )

    @property
    def likes_count(self):
        return len(self.likes)
    
    @property
    def comments_count(self):
        return len(self.comments)
    

    '''
    whats the @property ? 
    well normally if we do without @property , like this:
    def like_count(self):
        return len(self.likes) , it will require us to call post.likes_count() , with () notice

    but if we do it with @property, it will act as a instance variable call , 
    when we need to call it , we can call it as a variable , like post.likes_count , without ()
    '''