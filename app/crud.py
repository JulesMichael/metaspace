from sqlalchemy.orm import Session

from . import models, schemas

from datetime import date

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post