from fastapi import FastAPI
from app.db.database import  engine , Base
from app.api.routes.user import router as user_router
from app.api.routes.post import router as post_router
from app.api.routes.comment import router as comment_router
from app.db.models.post import Post #why are we importing models who ? we aint using them , so why
from app.db.models.user import User #its because the models  imported will be used to create table from metadata
from app.db.models.comment import Comment

Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(user_router) 
app.include_router(post_router)
app.include_router(comment_router)


@app.get('/')
def home():
    return {
        "message" : "currently working on backend , so please check redoc for more info !"
    }
