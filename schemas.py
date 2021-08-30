from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None
    disabled: bool = False

    class Config:
        orm_mode = True


class UserCreate(User):
    password: str


class UserInDB(User):
    hashed_password: str
