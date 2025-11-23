from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.base import Base

def setup_db():
    Base.metadata.create_all(engine)

engine = create_engine("sqlite:///database.sqlite", echo=True)
session = Session(bind=engine)