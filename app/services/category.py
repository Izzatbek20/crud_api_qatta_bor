from app.core.base import BaseService
from app.repositories.category import CategoryRepository
from app.core.exception import CreatedResponse, UpdatedResponse, DeletedResponse, NotFoundResponse
from app.schemas.category import CategoryStatus

from app.utils.pagination import PageParams

class CategoryService(BaseService[CategoryRepository]):
    async def get_all(self, status: CategoryStatus, title: str = None, parent_id: int = 0, page_params: PageParams = None):
        return await self.repository.get_all(status, title, parent_id, page_params)

    async def get_one(self, id: int):
        return await self.repository.get_one(id)

    async def create(self, payload: dict):
        await self.repository.create(payload)
        return CreatedResponse()

    async def update(self, id: int, payload: dict):
        result = await self.repository.get_one(id)
        if not result:
            return NotFoundResponse()
        else:
            await self.repository.create(payload)
            return UpdatedResponse()

    async def delete(self, id: int):
        result = await self.repository.get_one(id)
        if not result:
            return NotFoundResponse()
        else:
            await self.repository.delete(id)
            return DeletedResponse()