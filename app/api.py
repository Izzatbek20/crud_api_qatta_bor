from fastapi import APIRouter

# Auth
from .auth.login import auth_route

api = APIRouter()   

# Auth
api.include_router(auth_route, tags=['Auth'])

# Boshqa routerlar
