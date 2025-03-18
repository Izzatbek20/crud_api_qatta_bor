from sqlalchemy import insert, update, delete
from sqlalchemy.future import select

from app.models.users import Users
from app.core.base import BaseRepository
from app.utils.pagination import PageParams, pagination

class UserRepository(BaseRepository):
    async def get_all(self, page_params: PageParams = None):
        """
            Userning barcha ma'lumotlarini olish
        """
        query = select(Users)

        if page_params:
            return await pagination(self.session, query, page_params)
        else:
            result = await self.session.execute(query)
            return result.scalars().all()
        
    async def get_one(self, id: int):
        """
            User haqida to'liq ma'lumot olish
        """
        query = select(Users).where(Users.id==id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Yangi user qo'shish
        """
        query = insert(Users).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True
        
    async def update(self, id: int, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Userni ma'lumotlarini yangilash
        """
        query = update(Users).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True
        
    async def delete(self, id: int):
        """
            Userni bazadan o'chirib yuborish
        """
        query = delete(Users).where(Users.id==id)
        await self.session.execute(query)
        await self.session.commit()