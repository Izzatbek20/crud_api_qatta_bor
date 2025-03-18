from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.services.category import CategoryService
from app.schemas.category import CategoryResponse
from app.deps import category_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/category", summary="Barcha categoriyalarni olish")
async def router_get_all(
    #current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: CategoryService = Depends(category_service_dp)
) -> Page[CategoryResponse]:
    return await _service.get_all(page_params)

@router.get("/category_one", summary="Aniq categoriyaning malumotlarni olish")
async def router_get_one(
    id: int,
    # current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: CategoryService = Depends(category_service_dp)
) -> CategoryResponse:
    return await _service.get_one(id)

@router.post("/category", summary="Yangi categoriya yaratish")
async def reouter_create(
    payload: CategoryResponse,
    # current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    return await _service.create(payload)

@router.put("/category", summary="Categoriya ma'lumotlarini yangilash")
async def reouter_update(
    id: int,
    payload: CategoryResponse,
    # current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    return await _service.create(id, payload)

@router.delete("/category", summary="Categoriyani o'chirish")
async def router_delete(
    id: int,
    # current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    return await _service.delete(id)