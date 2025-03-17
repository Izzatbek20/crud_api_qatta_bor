"""Module providing a function printing python version."""
from contextlib import asynccontextmanager

import uvicorn
import time

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import JSONResponse
from sqlalchemy import event

from app.utils.slack import send_slack_message
from app.core.config import config

from sqlalchemy.engine import Engine

# Api route
from app.api import api as api_route
from database.seeder import Seeder

seeder = Seeder()

description = f"""
{config.app.app_name} uchun api
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    print("App ishga tushti")
    # await seeder.seed()
    yield
    # Clean up the ML models and release the resources
    print("App o'chti")


app = FastAPI(
    title=config.app.app_name,
    description=description,
    version='1.0',
    contact={
        'name': 'Github code',
        'url': 'https://github.com/Izzatbek20/crud_api_qatta_bor',
    },
    lifespan=lifespan,
    docs_url='/docs',  # None o`chirish
    redoc_url='/redoc',  # None o`chirish
    debug=config.debug
)

# HTTP javoblarini siqish uchun ishlatiladi, bu resurslarni uzatishni tezlashtiradi va tarmoqli resurslarni tejaydi.
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=4)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Xatolik haqida ma'lumotlar olish
    exc_type = type(exc).__name__
    exc_message = str(exc)

    # Slacga yuborish
    send_slack_message(exc, exc_type, exc_message)

    # Foydalanuvchiga javob
    if not config.debug:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Serverda kutilmagan xatolik yuz berdi."}
        )


# before_cursor_execute event'ida vaqtni o'lchashni boshlash
@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    context._query_start_time = time.time()


# after_cursor_execute event'ida vaqtni o'lchashni tugatish va chop etish
@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total_time = time.time() - context._query_start_time
    print(f"Query executed in {total_time:.4f} seconds")
    print(f"-----------------------------------------")


@app.get('/')
async def main():
    return {
        'status': 200,
        'message': 'Crud group 👋'
    }

app.include_router(api_route)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=7000,
                log_level="info", reload=False)
