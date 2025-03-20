from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.services.article_saved import ArticleSavedService
from app.schemas.article_saved import ArticleSavedResponse, ArticleSavedPayload
from app.deps import saved_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/saved",summary="Barcha saqlangan artikllarni olish")
async def router_saved_get_all(
    article_id: int = None,
    tg_user_id: int = None,
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: ArticleSavedService = Depends(saved_service_dp)
) -> Page[ArticleSavedResponse]:
    return await _service.get_all(article_id, tg_user_id, page_params)

@router.get("/saved/{id}",summary="Saqlangan artikl haqida to'liq ma'lumot olish")
async def router_saved_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: ArticleSavedService = Depends(saved_service_dp)
) -> ArticleSavedResponse:
    return await _service.get_one(id)

@router.post("/saved/create",summary="Artiklni saqlanganlar'ga qo'shish")
async def router_saved_create(
    payload: ArticleSavedPayload,
    current_user: Users = Depends(get_current_user),
    _service: ArticleSavedService = Depends(saved_service_dp)
):
    return await _service.create(payload)

@router.put("/saved/{id}/update",summary="Saqlangan artiklni o'zgartirish")
async def router_saved_update(
    id: int,
    payload: ArticleSavedPayload,
    current_user: Users = Depends(get_current_user),
    _service: ArticleSavedService = Depends(saved_service_dp)
):
    return await _service.update(id, payload)

@router.delete("/saved/{id}/delete",summary="Artiklni saqlanganlar orasidan o'chirish")
async def router_saved_delete(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: ArticleSavedService = Depends(saved_service_dp)
):
    return await _service.delete(id)