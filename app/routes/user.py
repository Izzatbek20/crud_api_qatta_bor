from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.services.user import UserService
from app.schemas.user import UserResponse, UserPayload
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
    payload: UserPayload,
    #current_user: Users = Depends(get_current_user),
    _service: UserService = Depends(user_service_dp)
):
    return await _service.create(payload)

@router.put("/users/{id}/update",summary="Userni ma'lumotlarini yangilash")
async def router_user_update(
    id: int,
    payload: UserPayload,
    current_user: Users = Depends(get_current_user),
    _service: UserService = Depends(user_service_dp)
):
    return await _service.update(id, payload)

@router.delete("/users/{id}/delete",summary="Userni bazadan o'chirib yuborish")
async def router_user_delete(
    id: int,
    current_user: Users = Depends(get_current_user),
    _service: UserService = Depends(user_service_dp)
):
    return await _service.delete(id)
    