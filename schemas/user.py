from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr

from db.models import Role


class LoginForm(BaseModel):
    email: str
    password: str

class UserBase(BaseModel):
    role: Optional[Role]
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID
    role: Role

    class Config:
        from_attributes = True

