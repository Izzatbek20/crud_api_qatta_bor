from app.core.base import BaseService
from app.core.exception import CreatedResponse, UpdatedResponse, DeletedResponse, NotFoundResponse
from app.schemas.region import RegionStatus
from app.utils.pagination import PageParams

class RegionService(BaseService):
    async def get_all(self,status: RegionStatus, parent_id = 0, page_params: PageParams = None):
        print(await self.repository.get_all(status, parent_id, page_params))
        return await self.repository.get_all(status, parent_id, page_params)

    async def get_one(self, id: int):
        return await self.repository.get_one(id)

    async def create(self, payload: dict):
        await self.repository.create(payload.model_dump())
        return CreatedResponse()

    async def update(self, id: int, payload: dict):
        region = await self.repository.get_one(id)
        if not region:
            return NotFoundResponse()

        await self.repository.update(id, payload.model_dump())
        return UpdatedResponse()

    async def delete(self, id: int):
        region = await self.repository.get_one(id)
        if not region:
            return NotFoundResponse()

        await self.repository.delete(id)
        return DeletedResponse()