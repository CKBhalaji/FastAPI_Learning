from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import Settings

print(Settings().database_hostname)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.route)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}