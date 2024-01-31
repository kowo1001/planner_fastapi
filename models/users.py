from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event

# 사용자 모델 클래스 정의

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        name = "users"
    class Config:
        schema_extra = {
            "examle": {
                "email": "fastapi@packt.com",
                "password": "string!!!",
                "events": [],
            }
        }

# class User(BaseModel):
#     email: EmailStr
#     password: str
#     username: str
#     events: Optional[List[Event]] = None
    # 또는 List[Event] | None = None

# 사용자 로그인 모델 클래스 정의
# class UserSignIn(BaseModel):
#     email: EmailStr
#     password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        schema_extra = {
            "examle": {
                "email": "fastapi@packt.com",
                "password": "string!!!",
                "events": [],
            }
        }





