from pydantic import BaseModel
from datetime import datetime

class TgUserPayload(BaseModel):
    user_id: int
    chat_id: int
    region_id: int
    fullname: int
    username: int
    latitude: float
    longitude: float

class TgUsersResponse(TgUserPayload):
    created_at: datetime
    updated_at: datetime