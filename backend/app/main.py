from fastapi import FastAPI
from app.api.routes import upload


app = FastAPI()


app.include_router(upload.router)


@app.get("/")
def root():
    return {
        "message":"AI Workout Tracker API is running!"
    }