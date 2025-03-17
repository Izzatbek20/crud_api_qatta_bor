from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class ArticleMediaResponse(BaseModel):
    # id: int
    article_id: int
    url: str
    type: "ArticleType"
    created_at: datetime
    updated_at: datetime

class ArticleType(str, Enum):
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    TEXT = "text"