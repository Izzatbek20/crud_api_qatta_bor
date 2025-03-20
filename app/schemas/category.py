from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import List

from app.schemas.article import ArticleResponse

class CategoryUpdatePayload(BaseModel):
    parent_id: int | None
    title: str | None
    description: str | None
    photo: str | None

class CategoryCreatePayload(BaseModel):
    parent_id: int
    title: str
    description: str
    photo: str

class CategoryResponse(CategoryCreatePayload):
    id: int
    position: int
    status: "CategoryStatus"
    created_at: datetime
    updated_at: datetime

class CategoryStatus(str, Enum):
    AKTIV = "active"
    INACTIV = "inactive"
    DELETED = "deleted"