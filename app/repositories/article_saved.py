from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from app.core.base import BaseRepository
from app.models.article_saved import ArticleSaved
from app.models.article import Article
from app.models.tg_user import TgUsers
from app.utils.pagination import PageParams, pagination

class ArticleSavedRepository(BaseRepository):
    async def get_all(self,
                      article_id: int = None,
                      tg_user_id: int = None,
                      page_params: PageParams = None):
        """
            Barcha ma'lumotlarni olish
        """
        query = select(ArticleSaved).options(joinedload(ArticleSaved.article), joinedload(ArticleSaved.tg_user))

        if article_id:
            query = query.where(ArticleSaved.article_id==article_id)
        if tg_user_id:
            query = query.where(ArticleSaved.tg_user_id==tg_user_id)

        if page_params:
            return await pagination(self.session, query, page_params)
        else:
            result = await self.session.execute(query)
            return result.scalars().all()

    async def get_one(self, id: int):
        """
            Article bannerning to'liq ma'lumotlarini olish
        """
        query = select(ArticleSaved).where(ArticleSaved.id==id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Yangi article banner yaratish
        """
        query = insert(ArticleSaved).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True

    async def update(self, id: int, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Article banner ma'lumotini yangilash
        """
        query = update(ArticleSaved).where(ArticleSaved.id==id).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True

    async def delete(self, id: int):
        """
            Article banner ma'lumotlarini o'chirish
        """
        query = delete(ArticleSaved).where(ArticleSaved.id==id)
        await self.session.execute(query)
        await self.session.commit()