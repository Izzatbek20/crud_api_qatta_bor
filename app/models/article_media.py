from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base
from datetime import datetime
from app.schemas.article_media import ArticleType


class ArticleMedia(Base):
    __tablename__ = "article_media"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(Integer, ForeignKey("article.id"), nullable=False)
    url: Mapped[str] = mapped_column(String(500)) 
    type: Mapped[str] = mapped_column(String(75), default=ArticleType.TEXT, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)

    #Relatioships
    article = relationship("Article", back_populates="article_media")