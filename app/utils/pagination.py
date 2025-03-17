import math

from fastapi import Query
from sqlalchemy.future import select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, TypeVar, List

from pydantic import BaseModel

T = TypeVar("T")


class Page(BaseModel, Generic[T]):
    page: int
    page_size: int
    total_count: int
    total_pages: int
    data: List[T]


# Paganitsiya qabul qiladigan ma'lumotlar
class PageParams:
    def __init__(
            self,
            page: int,
            page_size: int
    ):
        self.page = page
        self.page_size = page_size


def get_page_params(
        page: int = Query(1, ge=1, description="Joriy sahifa raqami"),
        page_size: int = Query(10, ge=1, le=500, description="Har bir sahifadagi elementlar soni")
) -> PageParams:
    return PageParams(page=page, page_size=page_size)


async def pagination(session: AsyncSession, query, page_params: PageParams, total_count: int = None):
    page = page_params.page
    page_size = page_params.page_size

    if not total_count:
        # Jami sonini. "query.column_descriptions[0]['entity']" bu query yozilyotgan tableni qaytaradi. "query.whereclause" where chartini qaytaradi
        count_query = select(func.count()).select_from(query.column_descriptions[0]['entity'])

        if query.whereclause is not None:
            count_query = count_query.where(query.whereclause)

        count_result = await session.execute(count_query)
        total_count = count_result.scalar_one()

    # Paginatsiya sahifalari
    offset = (page - 1) * page_size
    query_pagination = query.limit(page_size).offset(offset)

    # Paginatsiya ma'lumotlari
    todos_result = await session.execute(query_pagination)
    data = todos_result.unique().scalars().all()  # unique() joinedload() ishlatilganda one to many bo'lganda ishlatish kerak

    return Page(
        page=page,
        page_size=page_size,
        total_count=total_count,
        total_pages=math.ceil(total_count / page_size),
        data=data
    )
