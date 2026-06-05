from app.db.database import Base
from sqlalchemy import Column , Integer , String , DateTime
from datetime import datetime , timezone
from sqlalchemy.orm import relationship

#NOTE FOR ME - the base which we created  , we are simply inheriting it to models so they can work
#over orm , also models are meta data . meaning classes are not tables yet , they are just table
#defination blueprint. now its just stored internally in sqlalchemy
#once , we do Base.metadata.create_all(bind  = engine) , then this orm passes to psycopg2 and 
#query run.

class User(Base):

    __tablename__ = 'users'

    id  = Column(Integer , primary_key=True)
    username = Column(String(50) , nullable=False , unique=True)
    email = Column(String(255) , nullable=False , unique=True)
    password_hash =  Column(String , nullable=False)
    created_at = Column(
        DateTime(timezone=True) , #means timezone awared timestamps
        default=lambda:datetime.now(timezone.utc) #get current time from UTC timezone
    )
    bio = Column(String(300) , nullable=True)
    profile_picture_url = Column(String , nullable = True)
    github_url = Column(String , nullable=True)
    linkedin_url = Column(String , nullable=True)

    #a user has many posts , 1 : n relationship

    posts = relationship(
        "Post" ,
        back_populates="author" #tells orom that user.posts -> post.author are 2 sides of relation ship
    )


    comments = relationship(
        'Comment',
        back_populates='author'
    )

    likes = relationship(
        'Like',
        back_populates='user'
    )

    following = relationship(
        'Follow',
        foreign_keys='Follow.follower_id',
        back_populates='follower'
    )

    followers = relationship(
        'Follow',
        foreign_keys='Follow.following_id',
        back_populates='following'
    )

    @property
    def followers_count(self):
        return len(self.followers)
    
    @property
    def following_count(self):
        return len(self.following)


    sent_messages = relationship(
        'Message',
        foreign_keys='Message.sender_id',
        back_populates='sender'
    )

    received_messages = relationship(
        'Message',
        foreign_keys='Message.receiver_id',
        back_populates='receiver'
    )


