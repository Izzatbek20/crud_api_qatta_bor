from sqlalchemy import Integer, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
from datetime import datetime

class Queue(Base):
    __tablename__ = "queue"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(Integer, default = 0)
    is_channel: Mapped[bool] = mapped_column(Boolean, default=False)
    is_user: Mapped[bool] = mapped_column(Boolean, default=False)
    send_chat_id: Mapped[int] = mapped_column(Integer)
    region_id: Mapped[int] = mapped_column(Integer)
    body: Mapped[str] = mapped_column(Text)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)