from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
import os
from databases import Database
from sqlalchemy.orm import relationship


SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URI')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

users = Table(
    "users",
    metadata,
    Column("uid", String(255), primary_key=True),
    Column("email", String(100), unique=True),
    relationship("Project", back_populates="owner")
)


Base.metadata.create_all(bind=engine)

database = Database(SQLALCHEMY_DATABASE_URL)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
