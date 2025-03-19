from sqlalchemy.future import select
from sqlalchemy import insert, delete, update

from app.core.base import BaseRepository
from app.models.queue import Queue
from app.utils.pagination import PageParams, pagination

class QueueRepository(BaseRepository):
    async def get_all(self, page_params: PageParams = None):
        """
            Barcha ma'lumotlarni olish
        """
        query = select(Queue)

        if page_params:
            return await pagination(self.session, query, page_params)
        else:
            result = await self.session.execute(query)
            return result.scalars().all()

    async def get_one(self, id: int):
        """
            Queuening to'liq ma'lumotlarini olish
        """
        query = select(Queue).where(Queue.id==id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, payload: dict, flush: bool = False, commit: bool = True) -> int|bool:
        """
            Yangi Queue yaratish
        """
        query = insert(Queue).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]
        elif commit:
            await self.session.commit()
            return True

    async def update(self, id: int, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Queue ma'lumotlarini yangilash
        """
        query = update(Queue).where(Queue.id==id).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]
        elif commit:
            await self.session.commit()
            return True

    async def delete(self, id: int):
        """
            Ma'lumotlarni o'chirish
        """
        query = delete(Queue).where(Queue.id==id)
        await self.session.execute(query)
        await self.session.commit()
        return True