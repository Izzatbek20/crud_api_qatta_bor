from sqlalchemy import Integer, JSON, ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
from datetime import datetime
from app.schemas.article_banner import BannerType

class ArticleBanner(Base):
    __tablename__ = "article_banner"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(Integer, default = 0)
    urls: Mapped[str] = mapped_column(JSON)
    type: Mapped[str] = mapped_column(String(75), default=BannerType.IS_CONTENT, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)