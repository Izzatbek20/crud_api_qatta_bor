from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

#Services
from app.services.user import UserService
from app.services.article_banner import ArticleBannerService
from app.services.article import ArticleService

#Repositories
from app.repositories.user import UserRepository
from app.repositories.article_banner import ArticleBannerRepository
from app.repositories.article import ArticleRepository

from database.database import get_db

#User
def user_service_dp(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(repository=UserRepository(session=db))
#Article Banner
def banner_service_dp(db: AsyncSession = Depends(get_db)) -> ArticleBannerService:
    return ArticleBannerService(repository=ArticleBannerRepository(session=db))
#Article
def article_service_dp(db: AsyncSession = Depends(get_db)) -> ArticleService:
    return ArticleService(repository=ArticleRepository(session=db))