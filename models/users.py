from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

# 사용자 모델 클래스 정의
class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: List[Event] | None = None

# 사용자 로그인 모델 클래스 정의
class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "examle": {
                "email": "fastapi@packt.com",
                "password": "string!!!",
                "events": [],
            }
        }





