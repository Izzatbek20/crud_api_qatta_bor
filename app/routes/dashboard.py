from fastapi import APIRouter, Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db
from app.auth.services import get_current_user
from app.models.users import Users
from app.models.article import Article
from app.models.tg_user import TgUsers

router = APIRouter()

@router.get("/dashboard",summary="Asosiy page uchun statistika")
async def router_count_data(
    db: AsyncSession = Depends(get_db),
    current_user: Users = Depends(get_current_user),
):
    number_of_articles = select(func.count(Article.id))
    number_of_tgusers = select(func.count(TgUsers.user_id))

    return {'number_of_articles':(await db.execute(number_of_articles)).scalar_one(),
            'number_of_tgusers':(await db.execute(number_of_tgusers)).scalar_one()}