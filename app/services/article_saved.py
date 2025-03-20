from app.core.base import BaseService
from app.core.exception import CreatedResponse, UpdatedResponse, DeletedResponse, NotFoundResponse

from app.utils.pagination import PageParams

class ArticleSavedService(BaseService):
    async def get_all(self,
    article_id: int = None,
    tg_user_id: int = None,
    page_params: PageParams = None):
        return await self.repository.get_all(article_id, tg_user_id, page_params)

    async def get_one(self, id: int):
        return await self.repository.get_one(id)

    async def create(self, payload: dict):
        await self.repository.create(payload.model_dump())
        return CreatedResponse()

    async def update(self, id: int, payload: dict):
        article_saved = self.repository.get_one(id)
        if not article_saved:
            return NotFoundResponse()

        await self.repository.update(id, payload.model_dump())
        return UpdatedResponse()

    async def delete(self, id: int):
        article_saved = self.repository.get_one(id)
        if not article_saved:
            return NotFoundResponse()

        await self.repository.delete(id)
        return DeletedResponse()