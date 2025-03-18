from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.services.article_media import ArticleMediaService
from app.schemas.article_media import ArticleMediaResponse
from app.deps import media_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/media",summary="Barcha artikl medialarini olish")
async def router_media_get_all(
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: ArticleMediaService = Depends(media_service_dp)
) -> Page[ArticleMediaResponse]:
    return await _service.get_all(page_params)

@router.get("/media/{id}",summary="Artiklning mediasi haqida to'liq ma'lumot olish")
async def router_banner_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: ArticleMediaService = Depends(media_service_dp)
) -> ArticleMediaResponse:
    return await _service.get_one(id)

# @router.post("/media/create",summary="Artiklga yangi media qo'shish")
# async def router_banner_create(
#     payload: ArticleMediaPayload,
#     current_user: Users = Depends(get_current_user),
#     _service: ArticleMediaService = Depends(media_service_dp)
# ):
#     return await _service.create(payload)

# @router.put("/media/{id}/update",summary="Artiklning media ma'lumotlarini yangilash")
# async def router_media_update(
#     id: int,
#     payload: ArticleMediaPayload,
#     current_user: Users = Depends(get_current_user),
#     _service: ArticleMediaService = Depends(media_service_dp)
# ):
#     return await _service.update(id, payload)

@router.delete("/media/{id}/delete",summary="Artiklning media malumotlarini bazadan o'chirish")
async def router_media_delete(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: ArticleMediaService = Depends(media_service_dp)
):
    return await _service.delete(id)