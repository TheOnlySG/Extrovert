from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from app.db.database import  engine , Base
from app.api.routes.user import router as user_router
from app.api.routes.post import router as post_router
from app.api.routes.comment import router as comment_router
from app.api.routes.like import router as like_router
from app.api.routes.follow import router as follow_router
from app.api.routes.message import router as message_router
from app.api.routes.feed import router as feed_router
from app.api.routes.conversation import router as conversation_router
from app.api.routes.websocket import router as websocket_router

from app.db.models.post import Post 
from app.db.models.user import User 
from app.db.models.comment import Comment
from app.db.models.follow import Follow
from app.db.models.message import Message
from app.db.models.like import Like

Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(user_router) 
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(like_router)
app.include_router(follow_router)
app.include_router(message_router)
app.include_router(feed_router)
app.include_router(conversation_router)
app.include_router(websocket_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get('/')
def home():
    return RedirectResponse(url="/static/index.html")

