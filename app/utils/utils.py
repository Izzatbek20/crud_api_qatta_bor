import uuid
from pathlib import Path
from typing import List, Optional, Any, Type

from fastapi import UploadFile, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import class_mapper

from app.models.users import Base
from app.core.config import config


def format_number(num):
    return f"{num:02d}"


async def save_file(folder: str, file: UploadFile):
    UPLOAD_DIR = Path(f"{config.static}/{folder}")
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"{uuid.uuid4()}_{file.filename}"

    file_path = UPLOAD_DIR / filename

    if file and file.content_type not in ['image/png', 'image/jpg', 'image/jpeg', 'image/svg']:
        raise HTTPException(
            status_code=420,
            detail="Rasim uchun quydagi formatlarga ruxsat berilgan: *.png, .*jpg, *.jpeg, *.svg"
        )

    try:
        # Save the file
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail="File could not be saved")

    return {"filename": filename, "path": str(file_path)}


def get_fields(model: Type[Base], schema: Type[BaseModel]) -> List[Optional[Any]]:
    schema_fields = set(schema.__fields__.keys())

    model_columns = {column.name for column in class_mapper(model).columns}

    result = [
        getattr(model, column, None)
        for column in schema_fields
        if column in model_columns and not hasattr(getattr(model, column, None), 'relationship')
    ]

    return result


def get_field_rest(model, row):
    # Pydantic modelining barcha maydon nomlarini olish
    fields = model.__fields__.keys()
    # Row obyektidagi qiymatlarni model ustunlari nomiga qarab dictionary ko'rinishida olish
    return {field: getattr(row, field, None) for field in fields}


def iprint(data: Any) -> None:
    print("==========================================================")
    print("Type:", type(data))
    print("----------------------------------------------------------")
    print()
    print(data)
    print()
    print("==========================================================")
