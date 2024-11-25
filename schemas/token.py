from pydantic import BaseModel

from db.models import Role

class Token(BaseModel):
    access_token: str
    role: Role

class TokenData(BaseModel):
    email: str | None = None
    role: str | None = None

