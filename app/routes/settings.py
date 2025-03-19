from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.schemas.settings import SettingsResponse, SettingsPayload
from app.services.settings import SettingsService
from app.deps import settings_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/settings",summary="Barcha sozlamalarni olish")
async def router_region_get_all(
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: SettingsService = Depends(settings_service_dp)
) -> Page[SettingsResponse]:
    return await _service.get_all(page_params)

@router.get("/settings/{id}",summary="Sozlamalar haqida to'liq ma'lumot olish")
async def router_region_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: SettingsService = Depends(settings_service_dp)
) -> Page[SettingsResponse]:
    return await _service.get_one(id)

# @router.post("/settings/create",summary="Yangi sozlama yaratish")
# async def router_article_create(
#     payload: SettingsPayload,
#     current_user: Users = Depends(get_current_user),
#     _service: SettingsService = Depends(settings_service_dp)
# ) -> Page[SettingsResponse]:
#     return await _service.create(payload)

# @router.put("/settings/{id}/update",summary="Sozlama ma'lumotlarini yangilash")
# async def router_article_update(
#     id: int,
#     payload: SettingsPayload,
#     current_user: Users = Depends(get_current_user),
#     _service: SettingsService = Depends(settings_service_dp)
# ) -> Page[SettingsResponse]:
#     return await _service.get_all(id, payload)

@router.delete("/settings/{id}/delete",summary="Sozlama o'chirish")
async def router_settings_delete(
    id: int,
    current_service: Users = Depends(get_current_user),
    _service: SettingsService = Depends(settings_service_dp)
):
    return await _service.delete(id)