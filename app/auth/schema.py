from datetime import datetime
from pathlib import Path
from typing import Union, Optional
from pydantic import BaseModel, field_validator

from app.core.config import config


class Token(BaseModel):
    access_token: str
    token_type: str


class Refresh(BaseModel):
    token: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    phone: Union[str, None] = None
    fullname: Union[str, None] = None
    status: Union[bool, None] = None

class UserResponse(BaseModel):
    id: int
    username: str
    fullname: Optional[str] = None
    phone: Optional[int] = None
    filial_id: Optional[int] = None
    img: Optional[str] = None

    created_at: Union[datetime] = None

    @field_validator('img', mode='before')
    def image_base_url(cls, v):
        if v:
            v = Path(v).as_posix()
            return f"{config.app.app_url}/{v}"
        return v


class TokenResponse(BaseModel):
    user: UserResponse
    role: str
    token_type: str
    access_token: str
    refresh_token: str


class ImmResponse(BaseModel):
    detail: str
