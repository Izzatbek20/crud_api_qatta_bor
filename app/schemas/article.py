from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ArticleStatus(str, Enum):
    INACTIV = "inactived"
    WAIT = "waiting"
    PUBLISH = "published"
    DELETE = "deleted"

class ArticleUpdatePayload(BaseModel):
    author_id: int
    categorie_id: int
    region_id: int
    is_ad: bool
    is_ad_url: str
    title: str
    body: str
    latitude: float | None
    longitude: float | None
    start_date: datetime
    end_date: datetime

class ArticleCreatePayload(BaseModel):
    author_id: int
    categorie_id: int
    region_id: int
    is_ad: bool
    is_ad_url: str
    title: str
    body: str
    status: ArticleStatus
    latitude: float | None
    longitude: float | None
    start_date: datetime
    end_date: datetime

class ArticleTitleResponse(BaseModel):
    id: int
    title: str

class ArticleResponse(ArticleCreatePayload):
    id: int
    views: int
    created_at: datetime
    updated_at: datetime