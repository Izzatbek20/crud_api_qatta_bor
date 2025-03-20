from fastapi import Depends, APIRouter, Form, UploadFile, File
from typing import Union

from app.utils.utils import save_file
from app.auth.services import get_current_user
from app.models.users import Users
from app.services.user import UserService
from app.schemas.user import UserResponse, UserPayload, UserRole, UserStatus
from app.deps import user_service_dp
from app.utils.pagination import PageParams, get_page_params, Page

router = APIRouter()

@router.get("/users",summary="Userning barcha ma'lumotlarini olish")
async def router_user_get_all(
    current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: UserService = Depends(user_service_dp)
) -> Page[UserResponse]:
    return await _service.get_all(page_params)

@router.get("/users/{id}",summary="User haqida to'liq ma'lumot olish")
async def router_user_get_one(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: UserService = Depends(user_service_dp)
) -> UserResponse:
    return await _service.get_one(id)

@router.post("/users/create",summary="Yangi foydalanuvchi yaratish")
async def router_user_create(
    name: str = Form(description="Name",repr=False),
    username: str = Form(description="Description",repr=False),
    password_hash: str = Form(description="Password",repr=False),
    role: UserRole = Form(description="User role",repr=False),
    photo: Union[UploadFile, str, None] = File(None, description="photo"),
    status: UserStatus = Form(description="User status",repr=False),
    current_user: Users = Depends(get_current_user),
    _service: UserService = Depends(user_service_dp)
):
    payload = {
        "name":name,
        "username":username,
        "password_hash":password_hash,
        "role":role,
        "photo":photo,
        "status":status
    }

    if photo:
        save_image_path = await save_file('user_photo',photo)
        payload['photo'] = save_image_path['path']

    return await _service.create(payload)

@router.put("/users/{id}/update",summary="Userni ma'lumotlarini yangilash")
async def router_user_update(
    id: int,
    name: str = Form(description="Name",repr=False),
    username: str = Form(description="Description",repr=False),
    password_hash: str = Form(description="Password",repr=False),
    role: UserRole = Form(description="User role",repr=False),
    photo: Union[UploadFile, str, None] = File(None, description="photo"),
    status: UserStatus = Form(description="User status",repr=False),
    current_user: Users = Depends(get_current_user),
    _service: UserService = Depends(user_service_dp)
):
    payload = {
        "name":name,
        "username":username,
        "password_hash":password_hash,
        "role":role,
        "photo":photo,
        "status":status
    }

    if photo:
        save_image_path = await save_file('user_photo',photo)
        payload['photo'] = save_image_path['path']

    return await _service.update(id, payload)

@router.delete("/users/{id}/delete",summary="Userni bazadan o'chirib yuborish")
async def router_user_delete(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: UserService = Depends(user_service_dp)
):
    return await _service.delete(id)
