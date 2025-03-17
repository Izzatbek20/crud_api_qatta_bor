from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.database import Base

class ArticleSaved(Base):
    __tablename__ = "article_saved"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(Integer, ForeignKey("article.id"), nullable=False)
    tg_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("tg_users.id"), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)