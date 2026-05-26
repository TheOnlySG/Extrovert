from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {
        "message" : "starting a social media project -- backend focused."
    }
