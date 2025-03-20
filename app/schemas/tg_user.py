from pydantic import BaseModel
from datetime import datetime

from app.schemas.region import RegionTitleResponse

class TgUsersResponse(BaseModel):
    user_id: int
    chat_id: int
    region_id: int
    fullname: str
    username: str
    latitude: float
    longitude: float
    region: RegionTitleResponse
    created_at: datetime
    updated_at: datetime

class TgUserPayload(BaseModel):
    user_id: int
    chat_id: int
    region_id: int
    fullname: str
    username: str
    latitude: float
    longitude: float