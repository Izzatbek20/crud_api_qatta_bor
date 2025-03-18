from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class ArticleBannerPayload(BaseModel):
    article_id: int
    urls: str
    type: "BannerType"

class ArticleBannerResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

class BannerType(str, Enum):
    IS_BANNER = "is_banner"
    IS_CONTENT = "is_content"