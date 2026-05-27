from fastapi import FastAPI
from app.db.database import SessionLocal , engine , Base
from app.db.models.user import User


Base.metadata.create_all(bind = engine)

app = FastAPI()

@app.get('/')
def home():
    return {
        "message" : "starting a social media project -- backend focused."
    }
