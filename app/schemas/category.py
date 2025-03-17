from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class CategoryResponse(BaseModel):
    # id: int
    position: int
    parent_id: int
    title: str
    description: str
    photo: str
    status: "CategoryStatus"
    created_at: datetime
    updated_at: datetime

class CategoryStatus(str, Enum):
    AKTIV = "actived"
    INACTIV = "inactived"
    DELETE = "deleted"