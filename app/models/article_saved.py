from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from database.database import Base

class ArticleSaved(Base):
    __tablename__ = "article_saved"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(Integer, ForeignKey("articles.id"), nullable=False)
    tg_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("tg_users.user_id"), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())

    #Relationships
    article = relationship("Article", back_populates="article_saved")
    tg_user = relationship("TgUsers", back_populates="article_saved")