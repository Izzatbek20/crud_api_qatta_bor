from fastapi import Depends, APIRouter, UploadFile, File, Form
from typing import Union

from app.auth.services import get_current_user
from app.models.users import Users
from app.services.category import CategoryService
from app.schemas.category import CategoryResponse, CategoryCreatePayload, CategoryUpdatePayload, CategoryStatus
from app.deps import category_service_dp
from app.utils.utils import save_file
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/category", summary="Barcha categoriyalarni olish")
async def router_get_all(
    status: CategoryStatus,
    title: str = None,
    parent_id: int = 0,
    category_id: int = 0,
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: CategoryService = Depends(category_service_dp)
) -> Page[CategoryResponse]:
    return await _service.get_all(status, title, parent_id, category_id, page_params)

@router.get("/category/{id}", summary="Aniq categoriyaning malumotlarni olish")
async def router_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
) -> CategoryResponse:
    return await _service.get_one(id)

@router.post("/category/create", summary="Yangi categoriya yaratish")
async def reouter_create_category(
    parent_id: int = Form(description="Parent id",repr=False),
    title: str = Form(description="Title",repr=False),
    description: str = Form(description="Description",repr=False),
    photo: Union[UploadFile, str, None] = File(None, description="photo"),
    current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    payload = {
        'parent_id': parent_id,
        'title':title,
        'description':description,
        'photo':photo
    }

    if photo:
        rest = await save_file('category_photo',photo)
        payload['photo'] = rest['path']
    return await _service.create(payload)

@router.put("/category/{id}/update", summary="Categoriya ma'lumotlarini yangilash")
async def router_update_category(
    id: int,
    parent_id: int = Form(description="Parent id",repr=False),
    title: str = Form(description="Title",repr=False),
    description: str = Form(description="Description",repr=False),
    photo: Union[UploadFile, str, None] = File(None, description="photo"),
    current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    payload = {
        'parent_id': parent_id,
        'title':title,
        'description':description,
        'photo':photo
    }

    if photo:
        rest = await save_file('category_photo',photo)
        payload['photo'] = rest['path']
    return await _service.create(id, payload)

@router.put("/category/{id}/delete", summary="Categoriyani o'chirish")
async def router_delete_category(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: CategoryService = Depends(category_service_dp)
):
    return await _service.delete(id)