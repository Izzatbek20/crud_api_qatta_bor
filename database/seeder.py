import uuid

from sqlalchemy import insert, func
from sqlalchemy.future import select

from app.models.users import Users
from app.schemas.user import UserStatus, UserRole
from database.database import AsyncSessionLocal


class Seeder:

    async def seed(self):
        """
        Bazaga oldindan qo'shilishi kerak bo'lgan ma'lumotlarni qo'shib olamiz
        """
        async with AsyncSessionLocal() as db:
            await self.insert_admin(db)

    @staticmethod
    async def insert_admin(db: AsyncSessionLocal):
        # Branchlarni select qilish
        query = select(func.count(Users.id))
        user = await db.execute(query)
        user_count = user.scalar_one_or_none() or 0

        if not user_count:
            try:
                query = insert(Users).values({
                    'name': 'Supper Admin',
                    'role': UserRole.ADMIN,
                    'status': UserStatus.AKTIV,
                    'username': 'lemon',
                    'password_hash': '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW'
                })
                await db.execute(query)
                await db.commit()
            except Exception as e:
                await db.rollback()  # Xato yuzaga kelsa, tranzaksiyani orqaga qaytarish
                raise e  # Xatoni qaytarish
            finally:
                await db.close()  # Sessiyani yopish
