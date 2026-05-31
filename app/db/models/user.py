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

    #a user has many posts , 1 : n relationship

    posts = relationship(
        "Post" ,
        back_populates="author" #tells orom that user.posts -> post.author are 2 sides of relation ship
    )

