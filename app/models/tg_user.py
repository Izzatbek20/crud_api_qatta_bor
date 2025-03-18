from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base
from datetime import datetime

class TgUsers(Base):
    __tablename__ = "tg_users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, ForeignKey("user.id"), nullable=False)
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey("tg_chat.id"), nullable=False)
    region_id: Mapped[int] = mapped_column(Integer, ForeignKey("articles.id"), nullable=False)
    fullname: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)

    # Relations
    user = relationship("Users", back_populates="tg_users")
    chat = relationship("Chat", back_populates="tg_users")
    region = relationship("Region", back_populates="tg_users")
