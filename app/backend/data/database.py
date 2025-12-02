from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///data/database.sqlite", echo=True)
session = Session(bind=engine)