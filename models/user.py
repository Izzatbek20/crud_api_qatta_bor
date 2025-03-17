from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
from datetime import datetime
from schemas.user import UserStatus, UserRole

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(75), default=UserRole.ADMIN)
    #role user_role [note: "type tiniytext", default: "admin"]
    photo: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(75), default=UserStatus.AKTIV)
    #status status [note: "type tiniytext", default: "actived"]
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)