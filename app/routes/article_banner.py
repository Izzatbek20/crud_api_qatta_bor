from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.services.article_banner import ArticleBannerService
from app.schemas.article_banner import ArticleBannerResponse, ArticleBannerPayload
from app.deps import banner_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/banners",summary="Barcha bannerlarni olish")
async def router_banner_get_all(
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: ArticleBannerService = Depends(banner_service_dp)
) -> Page[ArticleBannerResponse]:
    return await _service.get_all(page_params)

@router.get("/banners/{id}",summary="Banner haqida to'liq ma'lumot olish")
async def router_banner_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: ArticleBannerService = Depends(banner_service_dp)
) -> ArticleBannerResponse:
    return await _service.get_one(id)

@router.post("/banners/create",summary="Yangi banner yaratish")
async def router_banner_create(
    payload: ArticleBannerPayload,
    current_user: Users = Depends(get_current_user),
    _service: ArticleBannerService = Depends(banner_service_dp)
):
    return await _service.create(payload)

@router.put("/banners/{id}/update",summary="Bannerni ma'lumotlarini yangilash")
async def router_banner_update(
    id: int,
    payload: ArticleBannerPayload,
    current_user: Users = Depends(get_current_user),
    _service: ArticleBannerService = Depends(banner_service_dp)
):
    return await _service.update(id, payload)

@router.delete("/banners/{id}/delete",summary="Bannerni bazadan o'chirish")
async def router_banner_delete(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: ArticleBannerService = Depends(banner_service_dp)
):
    return await _service.delete(id)