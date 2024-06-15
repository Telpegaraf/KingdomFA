from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from api_v1.schemas.character import Character


class UserBase(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None
    #characters: list[Character]


class UserRead(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr] = None
    is_active: bool


class UserUpdatePassword(BaseModel):
    old_password: str
    new_password: str


class User(UserBase):
    id: int
    model_config = ConfigDict(strict=True)
