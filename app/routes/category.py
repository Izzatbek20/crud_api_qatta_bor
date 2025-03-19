from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.services.category import CategoryService
from app.schemas.category import CategoryResponse, CategoryCreatePayload, CategoryUpdatePayload, CategoryStatus
from app.deps import category_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/category", summary="Barcha categoriyalarni olish")
async def router_get_all(
    status: CategoryStatus,
    parent_id: int = 0,
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: CategoryService = Depends(category_service_dp)
) -> Page[CategoryResponse]:
    return await _service.get_all(status, parent_id, page_params)

@router.get("/category/{id}", summary="Aniq categoriyaning malumotlarni olish")
async def router_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: CategoryService = Depends(category_service_dp)
) -> CategoryResponse:
    return await _service.get_one(id)

@router.post("/category/create", summary="Yangi categoriya yaratish")
async def reouter_create_category(
    payload: CategoryCreatePayload,
    current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    return await _service.create(payload)

@router.put("/category/{id}/update", summary="Categoriya ma'lumotlarini yangilash")
async def router_update_category(
    id: int,
    payload: CategoryUpdatePayload,
    current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    return await _service.create(id, payload)

@router.put("/category/{id}/delete", summary="Categoriyani o'chirish")
async def router_delete_category(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    return await _service.delete(id)