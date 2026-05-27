from fastapi import FastAPI
from app.db.database import SessionLocal , engine , Base
from app.db.models.user import User
from app.api.routes.user import router




Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(router) 



@app.get('/')
def home():
    return {
        "message" : "starting a social media project -- backend focused."
    }
