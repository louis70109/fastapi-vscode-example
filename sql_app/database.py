from sqlalchemy import MetaData, create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
import os
# from databases import Database


SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URI')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
Base = declarative_base()

Base.metadata.create_all(bind=engine)
# database = Database(SQLALCHEMY_DATABASE_URL)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
