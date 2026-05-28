from fastapi import FastAPI
from app.db.database import  engine , Base
from app.api.routes.user import router




Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(router) 



@app.get('/')
def home():
    return {
        "message" : "starting a social media project -- backend focused."
    }
