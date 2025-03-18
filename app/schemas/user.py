from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UserPayload(BaseModel):
    name: str
    username: str
    password: str
    role: "UserRole"
    photo: str
    status: "UserStatus"

class UserResponse(UserPayload):
    id: int
    created_at: datetime
    updated_at: datetime

class UserStatus(str, Enum):
    AKTIV = "actived"
    INACTIV = "inactived"
    DELETE = "deleted"

class UserRole(str, Enum):
    ADMIN = "admin"