from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type


async def object_list(
        model: Type,
        session: AsyncSession
):
    stmt = select(model).order_by('id')
    result: Result = await session.execute(stmt)
    objects = result.scalars().all()
    return list(objects)
