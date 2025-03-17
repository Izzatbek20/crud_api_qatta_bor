from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from database.database import get_db

# User
# def user_service_dp(db: AsyncSession = Depends(get_db)) -> UserService:
#     return UserService(repository=UserRepository(session=db))
