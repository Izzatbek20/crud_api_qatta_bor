from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import Base
from datetime import datetime
from app.models.region import Region
from app.models.queue import Queue
from app.schemas.article import ArticleStatus

class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    categorie_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=False)
    region_id: Mapped[int] = mapped_column(Integer, ForeignKey("region.id"), nullable=False)
    is_ad: Mapped[bool] = mapped_column(Boolean, default=False)
    is_ad_url:Mapped[str] = mapped_column(String(500))
    title: Mapped[str] = mapped_column(String(255))
    body: Mapped[str] = mapped_column(Text)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    views: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(String(75), default=ArticleStatus.WAIT)
    #status article_status [note: "type tiniytext", default: "waiting"]
    start_date: Mapped[DateTime] = mapped_column(DateTime) #datetime [note: "Maqolani ko'rinish vaqti"]
    end_date: Mapped[DateTime] = mapped_column(DateTime) #datetime [note: "Maqolani ko'rinish vaqti"]
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)

    #Relationship
    user = relationship("Users", back_populates="article")
    category = relationship("Category", back_populates="article")
    region = relationship("Region", back_populates="article")
    queue = relationship("Queue", back_populates="article", lazy='joined')
    article_banner = relationship("ArticleBanner", back_populates="article")
    article_media = relationship("ArticleMedia", back_populates="article")
    article_saved = relationship("ArticleSaved", back_populates="article")
    article_view = relationship("ArticleView", back_populates="article")
