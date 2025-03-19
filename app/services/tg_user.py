from app.core.base import BaseService
from app.core.exception import CreatedResponse, UpdatedResponse, DeletedResponse, NotFoundResponse
from app.utils.pagination import PageParams

class TgUserService(BaseService):
    async def get_all(self, page_params: PageParams = None):
        return await self.repository.get_all(page_params)
    
    async def get_one(self, id: int):
        return await self.repository.get_one(id)
    
    async def create(self, payload: dict):
        await self.repository.create(payload.model_dump())
        return CreatedResponse()
    
    async def update(self, id: int, payload: dict):
        tg_user = await self.repository.get_one(id)
        if not tg_user:
            return NotFoundResponse()
        
        await self.repository.update(id, payload.model_dump())
        return UpdatedResponse()

    async def delete(self, id: int):
        tg_user = await self.repository.get_one(id)
        if not tg_user:
            return NotFoundResponse()
    
        await self.repository.delete(id)
        return DeletedResponse()