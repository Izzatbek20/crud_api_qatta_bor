from pydantic import BaseModel
from datetime import datetime

class ArticleSavedPayload(BaseModel):
    article_id: int
    tg_user_id: int

class ArticleSavedResponse(ArticleSavedPayload):
    id: int
    created_at: datetime
    updated_at: datetime