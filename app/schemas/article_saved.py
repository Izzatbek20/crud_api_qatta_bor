from pydantic import BaseModel
from datetime import datetime
from app.schemas.article import ArticleTitleResponse

class ArticleSavedPayload(BaseModel):
    article_id: int
    tg_user_id: int

class ArticleSavedResponse(ArticleSavedPayload):
    id: int
    article: ArticleTitleResponse
    created_at: datetime
    updated_at: datetime