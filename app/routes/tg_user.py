from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.schemas.tg_user import TgUsersResponse, TgUserPayload
from app.services.tg_user import TgUserService
from app.deps import tguser_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/tg_users",summary="Barcha Telegram userlarni olish")
async def router_region_get_all(
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: TgUserService = Depends(tguser_service_dp)
) -> Page[TgUsersResponse]:
    return await _service.get_all(page_params)

@router.get("/tg_users/{id}",summary="Telegram user haqida to'liq ma'lumot olish")
async def router_region_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: TgUserService = Depends(tguser_service_dp)
) -> Page[TgUsersResponse]:
    return await _service.get_one(id)

@router.post("/tg_users/create",summary="Yangi telegram user uchun malumot yaratish")
async def router_article_create(
    payload: TgUserPayload,
    current_user: Users = Depends(get_current_user),
    _service: TgUserService = Depends(tguser_service_dp)
) -> Page[TgUsersResponse]:
    return await _service.create(payload)

@router.put("/tg_user/{id}/update",summary="Telegram user ma'lumotlarini yangilash")
async def router_article_update(
    id: int,
    payload: TgUserPayload,
    current_user: Users = Depends(get_current_user),
    _service: TgUserService = Depends(tguser_service_dp)
) -> Page[TgUsersResponse]:
    return await _service.get_all(id, payload)

@router.delete("/tg_users/{id}/delete",summary="Telegram user malumotlarini bazadan o'chirish")
async def router_article_delete(
    id: int,
    current_service: Users = Depends(get_current_user),
    _service: TgUserService = Depends(tguser_service_dp)
):
    return await _service.delete(id)