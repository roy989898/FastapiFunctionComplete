from typing import Optional

from pydantic import BaseModel, validator, StrictBool, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


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


class SignupForm(BaseModel):
    username: str
    full_name: str
    password: str
    password2: str
    isEmailUnique: StrictBool
    email: EmailStr

    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v

    @validator('email')
    def check_is_email_unique(cls, v, values):
        if not values['isEmailUnique']:
            raise ValueError('email is not unique')
        return v
