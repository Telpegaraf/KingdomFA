from fastapi import Path, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Type, TypeVar

from api_v1.models.enum import ModelNameDescription, model_name_description_mapping
from database import db_helper

T = TypeVar('T')


async def get_object_by_id(
        model: Type,
        object_id: int,
        session: AsyncSession,
):
    result = await session.execute(select(model).filter_by(id=object_id))
    obj = result.scalars().first()
    if obj is not None:
        return obj
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{model.__name__} with ID {object_id} isn't found",
    )


def get_object_by_id_dependency(model: Type[T]):
    async def dependency(
            object_id: int = Path(...),
            session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> T:
        return await get_object_by_id(model=model, object_id=object_id, session=session)
    return dependency
