from pydantic import BaseModel
from datetime import datetime

class ArticleSavedResponse(BaseModel):
    #id: int
    article_id: int
    tg_user_id: int
    created_at: datetime
    updated_at: datetime