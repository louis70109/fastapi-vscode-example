from typing import List, Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    account: str
    repository: str
    owner_id: Optional[str]


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    uid: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    # Projects: List[Project] = []

    class Config:
        orm_mode = True
