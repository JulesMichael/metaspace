from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from typing import List, Optional

from . import crud, models, schemas
from .database import SessionLocal, engine

# Crypto
from ecdsa import SigningKey
import jwt

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Consult the micro-blog
@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to my blog API !"}

@app.get("/stories")
async def get_stories() -> dict:
    return {"id":id}

@app.get("/stories/{id}")
async def get_single_story(id:int = None) -> dict:
    return {"id":id}

@app.get("/posts")
async def get_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> dict:
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}")
async def get_single_post(post_id, db: Session = Depends(get_db)) -> dict:
    db_post = crud.get_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.get("/feed")
async def feed() -> dict:
    """
        Return the JSON feed of the micro-blog
    """
    return {"id"}

# Create new entry

# update

# Delet 


