from sqlalchemy import insert, update, delete
from sqlalchemy.future import select

from app.core.base import BaseRepository
from app.models.region import Region
from app.schemas.region import RegionStatus
from app.utils.pagination import PageParams, pagination

class RegionRepository(BaseRepository):
    async def get_all(self, status: RegionStatus, parent_id: int, page_params: PageParams = None):
        """
            Barcha Regionlarni olish
        """
        query = select(Region).where(Region.parent_id==0).where(Region.status==status)

        if parent_id != 0 and status:
            query = select(Region).where(Region.parent_id==parent_id).where(Region.status==status)

        if page_params:
            return await pagination(self.session, query, page_params)
        else:
            result = await self.session.execute(query)
            return result.scalars().all()

    async def get_one(self, id: int):
        """
            Region haqida to'liq ma'lumot olish
        """
        query = select(Region).where(Region.id==id)
        result = await self.session.execute(query)
        return result.scalar()

    async def create(self, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Yangi region yaratish
        """
        query = insert(Region).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True

    async def update(self, id: int, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Region ma'lumotlarini yangilash
        """
        query = update(Region).where(Region.id==id).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]  # Flush qilinganda qo'shilgan ma'lumot id sini qaytaradi
        elif commit:
            await self.session.commit()
            return True

    async def delete(self, id: int):
        """
            Region o'chirish
        """
        value = {"status": RegionStatus.DELETE}
        query = update(Region).where(Region.id==id).values(value)
        await self.session.execute(query)
        await self.session.commit()