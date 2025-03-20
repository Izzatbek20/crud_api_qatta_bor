from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base
from datetime import datetime

class TgUsers(Base):
    __tablename__ = "tg_users"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    chat_id: Mapped[int] = mapped_column(Integer, nullable=False)
    region_id: Mapped[int] = mapped_column(Integer, ForeignKey('region.id'))
    fullname: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)

    # Relations
    #chat = relationship("Chat", back_populates="tg_users")
    user = relationship("Users", primaryjoin="Users.id==TgUsers.user_id" ,back_populates="tg_users")
    article_view = relationship("ArticleView",back_populates="tg_user")
    article_saved = relationship("ArticleSaved",back_populates="tg_user")
    region = relationship("Region", primaryjoin="TgUsers.region_id==Region.id", back_populates="tg_users")
