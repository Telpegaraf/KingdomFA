from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type
from api_v1.schemas.general import GeneralDescriptionBase, GeneralBase


async def object_list(
        model: Type,
        session: AsyncSession
):
    stmt = select(model).order_by('id')
    result: Result = await session.execute(stmt)
    objects = result.scalars().all()
    return list(objects)


async def object_create(
        session: AsyncSession,
        object_in: GeneralBase,
        model: Type
):
    object = model(**object_in.model_dump())
    session.add(object)
    await session.commit()
    await session.refresh(object)
    return object


async def object_with_description_create(
        session: AsyncSession,
        object_in: GeneralDescriptionBase,
        model: Type
):
    object = model(**object_in.model_dump())
    session.add(object)
    await session.commit()
    await session.refresh(object)
    return object
