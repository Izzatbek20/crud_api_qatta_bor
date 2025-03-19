from pydantic import BaseModel
from datetime import datetime

class SettingsResponse(BaseModel):
    # id: int
    channels: str
    created_at: datetime
    updated_at: datetime

class SettingsPayload(SettingsResponse):
    pass