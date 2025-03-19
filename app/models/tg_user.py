from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base
from datetime import datetime

class TgUsers(Base):
    __tablename__ = "tg_users"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey("tg_chat.id"), nullable=False)
    region_id: Mapped[int] = mapped_column(Integer)
    fullname: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)

    # Relations
    #chat = relationship("Chat", back_populates="tg_users")
    user = relationship("Users", primaryjoin="Users.id==TgUsers.user_id" ,back_populates="tg_users")
    #region = relationship("Region", back_populates="tg_users")