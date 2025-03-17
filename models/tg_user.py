from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Text, Float
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
from datetime import datetime

class TgUsers(Base):
    __tablename__ = "tg_users"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False) #[not null, note: "Telegram user id"]
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey("tg_chat.id"), nullable=False) #[not null, note: "Telegram chat id"]
    region_id: Mapped[int] = mapped_column(Integer, ForeignKey("article.id"), nullable=False) #[not null, note: "Mintaqa id."]
    fullname: Mapped[str] = mapped_column(String(255)) #[note: "Telegramdagi user fullname"]
    username: Mapped[str] = mapped_column(String(255)) #[note: "Telegramdagi user username"]
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)