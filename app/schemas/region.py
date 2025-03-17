from pydantic import BaseModel
from datetime import datetime

class RegionResponse(BaseModel):
    # id: int
    title: str
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime