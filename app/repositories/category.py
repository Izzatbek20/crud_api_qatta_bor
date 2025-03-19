from sqlalchemy.future import select
from sqlalchemy import insert, delete, update

from app.core.base import BaseRepository
from app.models.category import Category
from app.schemas.category import CategoryStatus
from app.utils.pagination import PageParams, pagination

class CategoryRepository(BaseRepository):
    async def get_all(self, status: CategoryStatus, parent_id: int = 0, page_params: PageParams = None):
        """
            Barcha ma'lumotlarni olish
        """
        query = select(Category).where(Category.parent_id==0).where(Category.status==status)

        if parent_id != 0 and status:
            query = select(Category).where(Category.parent_id==parent_id).where(Category.status==status)

        if page_params:
            return await pagination(self.session, query, page_params)
        else:
            result = await self.session.execute(query)
            return result.scalars().all()

    async def get_one(self, id: int):
        """
            Categoryning to'liq ma'lumotlarini olish
        """
        query = select(Category).where(Category.id==id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, payload: dict, flush: bool = False, commit: bool = True) -> int|bool:
        """
            Yangi category yaratish
        """
        query = insert(Category).values(payload)
        exc = await self.session.execute(query)

        if flush:
            await self.session.flush()
            return exc.inserted_primary_key[0]
        elif commit:
            await self.session.commit()
            return True

    async def update(self, id: int, payload: dict, flush: bool = False, commit: bool = True) -> int | bool:
        """
            Category ma'lumotlarini yangilash
        """
        query = update(Category).where(Category.id==id).values(payload)
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
        value = {'status':CategoryStatus.DELETED}
        query = update(Category).where(Category.id==id).values(value)
        await self.session.execute(query)
        await self.session.commit()
        return True