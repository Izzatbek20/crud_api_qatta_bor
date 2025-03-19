from fastapi import Depends, APIRouter

from app.auth.services import get_current_user
from app.models.users import Users
from app.services.queue import QueueService
from app.schemas.queue import QueueResponse
from app.deps import queue_service_dp
from app.utils.pagination import Page, PageParams, get_page_params

router = APIRouter()

@router.get("/queue", summary="Barcha queuelarni olish")
async def router_get_all(
    #current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: QueueService = Depends(queue_service_dp)
) -> Page[QueueResponse]:
    return await _service.get_all(page_params)

@router.get("/queue_one", summary="Aniq cqueuening malumotlarni olish")
async def router_get_one(
    id: int,
    # current_user: Users = Depends(get_current_user),
    page_params: PageParams = Depends(get_page_params),
    _service: QueueService = Depends(queue_service_dp)
) -> QueueResponse:
    return await _service.get_one(id)

@router.post("/queue", summary="Yangi queue yaratish")
async def reouter_create(
    payload: QueueResponse,
    # current_user: Users = Depends(get_current_user),
    _service: QueueService = Depends(queue_service_dp)
):
    return await _service.create(payload)

@router.put("/queue", summary="queue ma'lumotlarini yangilash")
async def reouter_update(
    id: int,
    payload: QueueResponse,
    # current_user: Users = Depends(get_current_user),
    _service: QueueService = Depends(queue_service_dp)
):
    return await _service.create(id, payload)

@router.delete("/queue", summary="queueni o'chirish")
async def router_delete(
    id: int,
    # current_user: Users = Depends(get_current_user),
    _service: QueueService = Depends(queue_service_dp)
):
    return await _service.delete(id)