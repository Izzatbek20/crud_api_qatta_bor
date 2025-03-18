from fastapi import APIRouter

# Auth
from .auth.login import auth_route

from app.routes import user, article_banner

api = APIRouter()   

# Auth
api.include_router(auth_route, tags=['Auth'])

# Boshqa routerlar
api.include_router(user.router, tags=["User"])
api.include_router(article_banner.router, tags=["Article banner"])