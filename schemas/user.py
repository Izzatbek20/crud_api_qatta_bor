from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UserResponse(BaseModel):
    #id: int
    name: str
    username: str
    password: str
    role: "UserRole"
    photo: str
    status: "UserStatus"
    created_at: datetime
    updated_at: datetime

class UserStatus(str, Enum):
    AKTIV = "actived"
    INACTIV = "inactived"
    DELETE = "deleted"

class UserRole(str, Enum):
    ADMIN = "admin"