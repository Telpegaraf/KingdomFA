from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.models.god import God
from api_v1.schemas.god import GodBase


async def god_create(god_in: GodBase, session: AsyncSession) -> God:
    god = God(**god_in.model_dump())
    session.add(god)
    await session.commit()
    await session.refresh(god)
    return god
