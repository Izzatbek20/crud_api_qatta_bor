from fastapi import APIRouter

# Auth
from .auth.login import auth_route

from app.routes import user, article_banner, article_media, article, article_saved, article_view, category, region, tg_user, settings

api = APIRouter()

# Auth
api.include_router(auth_route, tags=['Auth'])

# Boshqa routerlar
api.include_router(user.router, tags=["User"])
api.include_router(article.router, tags=["Article"])
api.include_router(article_banner.router, tags=["Article banner"])
api.include_router(article_media.router, tags=["Article media"])
api.include_router(article_saved.router, tags=["Article saved"])
api.include_router(article_view.router, tags=["Article view"])
api.include_router(category.router, tags=["Category"])
api.include_router(region.router, tags=["Region"])
api.include_router(tg_user.router, tags=["Telegram user"])
api.include_router(settings.router, tags=["Settings"])