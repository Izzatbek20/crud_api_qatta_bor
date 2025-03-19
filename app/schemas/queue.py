from pydantic import BaseModel
from datetime import datetime

class QueueResponse(BaseModel):

    #id: int
    article_id: int
    is_channel: bool
    is_user: bool
    send_chat_id: int
    region_id: int
    body: str
    created_at: datetime
    updated_at: datetime