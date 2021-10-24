from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, LargeBinary
from sqlalchemy.orm import relationship

from .database import Base

class Post:
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    author = Column(String)
    content = Column(String)
    
    attachements = relationship("Attachement", back_populates="corresponding_post")

class Attachement:
    __tablename__ =  "attachements"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    file_id = Column(Integer, ForeignKey("file.id"))

    corresponding_post = relationship("Post", back_populates="attachements")
    file = relationship("File")


class File:
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    minetype: Column(String)
    binarydata = Column(LargeBinary)


class Story:
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    file_id = Column(Integer, ForeignKey("file.id"))

    file = relationship("File")