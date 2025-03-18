from fastapi import APIRouter

# Auth
from .auth.login import auth_route

from app.routes import user, article_banner, article_media, article, article_saved, article_view, category

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