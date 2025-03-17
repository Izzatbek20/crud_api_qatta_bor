from sqlalchemy import Integer, JSON, ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
from datetime import datetime
from schemas.article_banner import BannerType

class ArticleBanner(Base):
    __tablename__ = "article_banner"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(Integer, ForeignKey("article.id"), nullable=False)
    urls: Mapped[str] = mapped_column(JSON) #json [note:
#       '''
#     ## Fayl manzili

#     Banner	960x540	16:9 \n
#     Maqola rasm	400x400	1:1\n
#     rasimlar json fayl ichida shunaqa nisbatda yuklanadi siqilgan

#     Rasim 3 ta bo'ladi ikkitasi yuqoridagilar. 1 ta rasimni asil xolati
#   ''']
    type: Mapped[str] = mapped_column(String(75), default=BannerType.IS_CONTENT, nullable=False) #banner_type [not null, default: 'is_content', note:'''
    # type `tiniytext`.\n\n
    # Banner turi\n

    # * **`is_banner`** - Reklama xisoblansa bannerda ko'rinadigan rasim
    # * **`is_content`** - Reklama bo'lmasa maqolalar orasida ko'rinadigan rasmi
    # ''']
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)