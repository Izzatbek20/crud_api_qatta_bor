from fastapi import Query
from sqlalchemy.future import select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, TypeVar, List, Optional

from pydantic import BaseModel

T = TypeVar("T")


class PageCursor(BaseModel, Generic[T]):
    cursor: int
    size: int
    count: int
    data: List[T]


I = TypeVar("I")


# With Metadata
class PageCursorWM(BaseModel, Generic[T, I]):
    cursor: int
    size: int
    count: int
    metadata: Optional[I] = None  # Filtrlash, saralash va statistikalar uchun qo'shimcha ma'lumotlar
    data: List[T]


# Paganitsiya qabul qiladigan ma'lumotlar
class PageCursorParams:
    def __init__(
            self,
            cursor: int,
            size: int
    ):
        self.cursor = cursor
        self.size = size


def get_page_params_cursor(
        cursor: int = Query(1, ge=1, description="Oxirgi ma'lumot `id`-si"),
        size: int = Query(10, ge=1, le=500, description="Har bir so'rovdagi elementlar soni")
) -> PageCursorParams:
    return PageCursorParams(cursor=cursor, size=size)


async def pagination_cursor(session: AsyncSession, query, page_params: PageCursorParams, scalars: bool = True,
                            total_count: int = None, union: bool = False, metadata: dict = None):
    # Where cursor shartimizda *.id > cursor qilingan. cursor=1 bo'lsa unda 1 element chiqme qoladi.
    # Shuning uchun cursor 1 kelsa uni qiymatini 0 qilib olamiz. 1 id element ko'rinishi uchun.
    cursor = page_params.cursor if page_params.cursor > 1 else 0
    size = page_params.size

    if total_count is None:
        # Jami sonini. "query.column_descriptions[0]['entity']" bu query yozilyotgan tableni qaytaradi. "query.whereclause" where shartini qaytaradi
        count_query = select(func.count()).select_from(query.column_descriptions[0]['entity'])

        if query.whereclause is not None:
            count_query = count_query.where(query.whereclause)

        count_result = await session.execute(count_query)
        total_count = count_result.scalar_one()

    if not union:
        # Paginatsiya sahifalari
        query_pagination = (
            query
            .where(query.column_descriptions[0]['entity'].id > cursor)
            .order_by(query.column_descriptions[0]['entity'].id.asc())
            .limit(size)
        )
    else:
        # Subquery qilish
        subquery = query.subquery()
        entity = subquery.c  # Ustunlarga kirish uchun .c ishlatiladi

        # Paginatsiya uchun so'rov
        query_pagination = (
            select(subquery)
            .where(entity.id > cursor)
            .order_by(entity.id.asc())
            .limit(size)
        )

    # Paginatsiya ma'lumotlari
    todos_result = await session.execute(query_pagination)
    if not scalars:
        data = todos_result.unique().all()  # unique() joinedload() ishlatilganda one to many bo'lganda ishlatish kerak
    else:
        data = todos_result.unique().scalars().all()  # unique() joinedload() ishlatilganda one to many bo'lganda ishlatish kerak

    if metadata:
        return PageCursorWM(
            cursor=cursor if cursor > 0 else 1,  # Cursor qiymati 0 bo'lmaydi shuning uchun 0 kelsa 1 qilib qayataramiz.
            size=size,
            count=total_count,
            data=data,
            metadata=metadata
        )
    else:
        return PageCursor(
            cursor=cursor if cursor > 0 else 1,  # Cursor qiymati 0 bo'lmaydi shuning uchun 0 kelsa 1 qilib qayataramiz.
            size=size,
            count=total_count,
            data=data
        )
