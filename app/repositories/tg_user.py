from sqlalchemy import insert, update, delete
from sqlalchemy.future import select

from app.core.base import BaseRepository
from app.models.tg_user import TgUsers
from app.utils.pagination import PageParams, pagination

class TgUserRepository(BaseRepository):
    async def get_all(self, page_params: PageParams = None):
        """
            Barcha Telegram userlarni olish
        """
        query = select(TgUsers)

        if page_params:
            return await pagination(self.session, query, page_params)
        else:
            result = await self.session.execute(query)
            return result.scalars().all()
        
    async def get_one(self, id: int):
        """
            TgUsers haqida to'liq ma'lumot olish
        """
        query = select(TgUsers).where(TgUsers.id==id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Yangi TgUsers yaratish
        """
        query = insert(TgUsers).values(payload)
        exc = await self.session.execute(query)
    
        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True
    
    async def update(self, id: int, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            TgUsers ma'lumotlarini yangilash
        """
        query = update(TgUsers).where(TgUsers.id==id).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True
        
    async def delete(self, id: int):
        """
            TgUsers o'chirish
        """
        query = delete(TgUsers).where(TgUsers.id==id)
        await self.session.execute(query)
        await self.session.commit()