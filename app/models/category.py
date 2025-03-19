from sqlalchemy import String, Integer, DateTime
from database.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.schemas.category import CategoryStatus

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    position: Mapped[int] = mapped_column(Integer, default=1)
    parent_id: Mapped[int] = mapped_column(Integer, default=0)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1000))
    photo: Mapped[str] = mapped_column(String(500))
    status: Mapped[str] = mapped_column(String(75), default=CategoryStatus.AKTIV)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())

    # Relationships
    article = relationship("Article", back_populates="category")