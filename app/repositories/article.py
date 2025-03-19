from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from datetime import date
from app.core.base import BaseRepository
from app.models.article import Article
from app.schemas.article import ArticleStatus
from app.utils.pagination import PageParams, pagination

class ArticleRepository(BaseRepository):
    async def get_all(self, status: ArticleStatus, page_params: PageParams = None):
        """
            Barcha articlelarni olish
        """
        query = select(Article).where(Article.status==status)

        if page_params:
            return await pagination(self.session, query, page_params)
        else:
            result = await self.session.execute(query)
            return result.scalars().all()

    async def get_one(self, id: int):
        """
            Article haqida to'liq ma'lumot olish
        """
        query = select(Article).where(Article.id==id)
        result = await self.session.execute(query)
        return result.unique().scalar_one_or_none()

    async def create(self, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Yangi article yaratish
        """
        query = insert(Article).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True

    async def update(self, id: int, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Article ma'lumotlarini yangilash
        """
        query = update(Article).where(Article.id==id).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True

    async def delete(self, id: int):
        """
            Articleni o'chirish
        """
        value = {"status": ArticleStatus.DELETE}
        query = update(Article).where(Article.id==id).values(value)
        await self.session.execute(query)
        await self.session.commit()