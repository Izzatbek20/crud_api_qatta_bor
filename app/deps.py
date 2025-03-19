from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

#Services
from app.services.user import UserService
from app.services.article_banner import ArticleBannerService
from app.services.article import ArticleService
from app.services.article_view import ArticleViewService
from app.services.article_saved import ArticleSavedService
from app.services.article_media import ArticleMediaService
from app.services.category import CategoryService
from app.services.region import RegionService
from app.services.settings import SettingsService
from app.services.tg_user import TgUserService

#Repositories
from app.repositories.user import UserRepository
from app.repositories.article_banner import ArticleBannerRepository
from app.repositories.article import ArticleRepository
from app.repositories.article_view import ArticleViewRepository
from app.repositories.article_saved import ArticleSavedRepository
from app.repositories.article_media import ArticleMediaRepository
from app.repositories.category import CategoryRepository
from app.repositories.region import RegionRepository
from app.repositories.settings import SettingsRepository
from app.repositories.tg_user import TgUserRepository

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
#Article View
def view_service_dp(db: AsyncSession = Depends(get_db)) -> ArticleViewService:
    return ArticleViewService(repository=ArticleViewRepository(session=db))
#Article Saved
def saved_service_dp(db: AsyncSession = Depends(get_db)) -> ArticleSavedService:
    return ArticleSavedService(repository=ArticleSavedRepository(session=db))
#Article Media
def media_service_dp(db: AsyncSession = Depends(get_db)) -> ArticleMediaService:
    return ArticleMediaService(repository=ArticleMediaRepository(session=db))
#Category
def category_service_dp(db: AsyncSession = Depends(get_db)) -> CategoryService:
    return CategoryService(repository=CategoryRepository(session=db))
#Region
def region_service_dp(db: AsyncSession = Depends(get_db)) -> RegionService:
    return RegionService(repository=RegionRepository(session=db))
#Settings
def settings_service_dp(db: AsyncSession = Depends(get_db)) -> SettingsService:
    return SettingsService(repository=SettingsRepository(session=db))
#Telegram user
def tguser_service_dp(db: AsyncSession = Depends(get_db)) -> TgUserService:
    return TgUserService(repository=TgUserRepository(session=db))