from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.schemas.article_view import ArticleViewResponse
from app.services.article_view import ArticleViewService
from app.deps import article_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/articles",summary="Barcha artikllarni olish")
async def router_articleview_get_all(
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: ArticleViewService = Depends(article_service_dp)
) -> Page[ArticleViewResponse]:
    return await _service.get_all(page_params)

@router.get("/articles/{id}",summary="Artik haqida to'liq ma'lumot olish")
async def router_articleview_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: ArticleViewService = Depends(article_service_dp)
) -> Page[ArticleViewResponse]:
    return await _service.get_one(id)

# @router.post("/articles/create",summary="Yangi artikl yaratish")
# async def router_articleview_create(
#     payload: ArticlePayload,
#     current_user: Users = Depends(get_current_user),
#     _service: ArticleViewService = Depends(article_service_dp)
# ) -> Page[ArticleViewResponse]:
#     return await _service.create(payload)

# @router.get("/articles/{id}/update",summary="Artikl ma'lumotlarini yangilash")
# async def router_articleview_update(
#     id: int,
#     payload: ArticlePayload,
#     current_user: Users = Depends(get_current_user),
#     _service: ArticleViewService = Depends(article_service_dp)
# ) -> Page[ArticleViewResponse]:
#     return await _service.get_all(id, payload)

@router.delete("/articles/{id}/delete",summary="Artiklni o'chirish")
async def router_articleview_delete(
    id: int,
    current_service: Users = Depends(get_current_user),
    _service: ArticleViewService = Depends(article_service_dp)
):
    return await _service.delete(id)