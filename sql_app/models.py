from sqlalchemy import Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship

id_seq = Sequence('id_seq')
from .database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(String(255), primary_key=True, unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    projects = relationship("Project", back_populates="owner")


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, id_seq, primary_key=True, unique=True, index=True)
    account = Column(String(100), index=True)
    repository = Column(String(100), index=True)
    owner_id = Column(String(255), ForeignKey("users.uid"))

    owner = relationship("User", back_populates="projects")
