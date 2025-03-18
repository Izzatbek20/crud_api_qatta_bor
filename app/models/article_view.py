from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base
from datetime import datetime

class ArticleView(Base):
    __tablename__ = "article_views"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(Integer, ForeignKey("articles.id"), nullable=False)
    tg_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("tg_users"), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)

    #Relationships
    article = relationship("Article", back_populates="article_view")
    tg_user = relationship("TgUsers", back_populates="article_view")