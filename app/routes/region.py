from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.schemas.region import RegionResponse, RegionCreatePayload, RegionUpdatePayload, RegionStatus
from app.services.region import RegionService
from app.deps import region_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/region",summary="Barcha regionlarni olish")
async def router_region_get_all(
    status: RegionStatus,
    parent_id = 0,
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: RegionService = Depends(region_service_dp)
) -> Page[RegionResponse]:
    return await _service.get_all(status, parent_id, page_params)

@router.get("/region/{id}",summary="Region haqida to'liq ma'lumot olish")
async def router_region_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: RegionService = Depends(region_service_dp)
) -> Page[RegionResponse]:
    return await _service.get_one(id)

@router.post("/region/create",summary="Yangi region yaratish")
async def router_article_create(
    payload: RegionCreatePayload,
    current_user: Users = Depends(get_current_user),
    _service: RegionService = Depends(region_service_dp)
) -> Page[RegionResponse]:
    return await _service.create(payload)

@router.put("/region/{id}/update",summary="Region ma'lumotlarini yangilash")
async def router_article_update(
    id: int,
    payload: RegionUpdatePayload,
    current_user: Users = Depends(get_current_user),
    _service: RegionService = Depends(region_service_dp)
) -> Page[RegionResponse]:
    return await _service.get_all(id, payload)

@router.delete("/region/{id}/delete",summary="Regionni o'chirish")
async def router_article_delete(
    id: int,
    current_service: Users = Depends(get_current_user),
    _service: RegionService = Depends(region_service_dp)
):
    return await _service.delete(id)