from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
from datetime import datetime

class Region(Base):
    __tablename__ = "region"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)