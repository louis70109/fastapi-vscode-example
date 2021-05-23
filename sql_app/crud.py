from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.uid == user_id).first()


def get_user_by_uid(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.uid == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(uid=user.uid, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()


def create_user_project(db: Session, project: schemas.ProjectCreate, user_id: str):
    project.owner_id = user_id
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_user_projects(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    return db.query(models.Project).filter(
        models.Project.owner_id == user_id).offset(skip).limit(limit).all()
