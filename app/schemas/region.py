from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class RegionUpdatePayload(BaseModel):
    parent_id: int
    title: str | None
    latitude: float | None
    longitude: float | None

class RegionCreatePayload(BaseModel):
    parent_id: int
    title: str
    latitude: float
    longitude: float

class RegionResponse(RegionCreatePayload):
    id: int
    status: "RegionStatus"
    created_at: datetime
    updated_at: datetime

class RegionStatus(str, Enum):
    ACTIV = "actived"
    INACTIV = "inactived"
    DELETE = "deleted"