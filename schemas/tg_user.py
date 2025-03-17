from pydantic import BaseModel
from datetime import datetime

class TgUsersResponse(BaseModel):
    user_id: int
    chat_id: int
    region_id: int
    fullname: int
    username: int
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime