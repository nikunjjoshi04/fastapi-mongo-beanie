from datetime import datetime
from typing import Optional

from beanie import Document
from pydantic import BaseModel, EmailStr


class User(Document):
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime = None
    updated_at: datetime = None

    class Settings:
        name = "users"


class UserCreate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Nikunj",
                "last_name": "Joshi",
                "email": "nikunj.joshi@edgevana.com",
            }
        }


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Nikunj",
                "last_name": "Joshi",
                "email": "nikunj.joshi@edgevana.com",
            }
        }
