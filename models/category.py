from sqlalchemy import String, Integer, ForeignKey, DateTime
from database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from schemas.category import CategoryStatus

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    position: Mapped[int] = mapped_column(Integer, default=1) #[default: 1, note:"Kategoriyani joylashish tartibi"]
    parent_id: Mapped[int] = mapped_column(Integer, default=0) #[default: 0, note: '''
    ## SubCategories
    #Ichki kategoriyalarni uchun. Eng yuqorida turgan kategoriya da bu qiymat 0 bo'lad. Ichki kategoriyada uni ota kategoriyasi idsi yoziladi
    #''']
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1000))
    photo: Mapped[str] = mapped_column(String(500))
    status: Mapped[str] = mapped_column(String(75), default=CategoryStatus.AKTIV)
    #status status [note: "type tiniytext", default: "actived"]
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime)