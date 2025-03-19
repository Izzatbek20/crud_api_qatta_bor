from sqlalchemy import insert, update, delete
from sqlalchemy.future import select

from app.core.base import BaseRepository
from app.models.settings import Settings
from app.utils.pagination import PageParams, pagination

class SettingsRepository(BaseRepository):
    async def get_all(self, page_params: PageParams = None):
        """
            Barcha sozlamalarni olish
        """
        query = select(Settings)

        if page_params:
            return await pagination(self.session, query, page_params)
        else:
            result = await self.session.execute(query)
            return result.scalars().all()
        
    async def get_one(self, id: int):
        """
            Sozlama haqida to'liq ma'lumot olish
        """
        query = select(Settings).where(Settings.id==id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Yangi sozlama yaratish
        """
        query = insert(Settings).values(payload)
        exc = await self.session.execute(query)
    
        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True
    
    async def update(self, id: int, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Sozlama ma'lumotlarini yangilash
        """
        query = update(Settings).where(Settings.id==id).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True
        
    async def delete(self, id: int):
        """
            Sozlamani o'chirish
        """
        query = delete(Settings).where(Settings.id==id)
        await self.session.execute(query)
        await self.session.commit()