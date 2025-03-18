from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class ArticleResponse(BaseModel):
    id: int
    author_id: int
    categorie_id: int
    region_id: int
    is_ad: bool
    is_ad_url: str
    title: str
    body: str
    latitude: float
    longitude: float
    views: int
    status: "ArticleStatus"
    start_date: datetime
    end_date: datetime
    created_at: datetime
    updated_at: datetime

class ArticleStatus(str, Enum):
    INACTIV = "inactived"
    WAIT = "waiting"
    PUBLISH = "published"
    DELETE = "deleted"