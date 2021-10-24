from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
db = os.environ["POSTGRES_DB"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@0.0.0.0/{db}"

print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

