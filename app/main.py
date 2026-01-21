from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routes import users
from .routes import auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "This is From Backend"} 

@app.get("/status")
def read_status():
    return {"status": "API is running"}

