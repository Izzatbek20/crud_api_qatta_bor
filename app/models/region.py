from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base
from datetime import datetime
from app.schemas.region import RegionStatus

class Region(Base):
    __tablename__ = "region"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    parent_id: Mapped[int] = mapped_column(Integer, default=0)
    title: Mapped[str] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(75), default=RegionStatus.ACTIV)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())

    #Relationships
    article = relationship("Article", back_populates="region")
    queue = relationship("Queue", back_populates="region")