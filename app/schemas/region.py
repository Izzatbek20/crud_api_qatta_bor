from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class RegionTitleResponse(BaseModel):
    id: int
    title: str

class RegionResponse(BaseModel):
    id: int
    title: str
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime

class RegionStatus(str, Enum):
    ACTIV = "actived"
    INACTIV = "inactived"
    DELETE = "deleted"

class RegionPayload(RegionResponse):
    pass