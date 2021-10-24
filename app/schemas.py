from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class PostBase(BaseModel):
    date : date
    author : str
    content : str 

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id : int
    attachements : List = []

    class Config:
        orm_mode = True