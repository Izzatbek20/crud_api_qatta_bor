from pydantic import BaseModel
from datetime import datetime

from app.schemas.region import RegionTitleResponse

class TgUsersResponse(BaseModel):
    user_id: int
    chat_id: int
    region_id: int
    fullname: int
    username: int
    latitude: float
    longitude: float
    region: RegionTitleResponse
    created_at: datetime
    updated_at: datetime

class TgUserPayload(TgUsersResponse):
    user_id: int
    chat_id: int
    region_id: int
    fullname: int
    username: int
    latitude: float
    longitude: float