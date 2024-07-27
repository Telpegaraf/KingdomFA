from fastapi import HTTPException
from typing import Type, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

T = TypeVar('T')


async def get_model_result(model: Type[T], object_id: int, session: AsyncSession):
    object_result = await session.execute(
        select(model).where(model.id == object_id)
    )
    object = object_result.scalar_one_or_none()
    if object is None:
        raise HTTPException(status_code=404, detail=f"{model.__name__} is not found")
    return object
