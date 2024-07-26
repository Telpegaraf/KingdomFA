from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type
from api_v1.schemas.race import RaceBase
from api_v1.models.race import Race


async def race_list(
        session: AsyncSession
):
    stmt = select(Race).order_by('id')
    result: Result = await session.execute(stmt)
    races = result.scalars().all()
    return list(races)


async def race_detail(
        session: AsyncSession,
        race_id: int
) -> Race:
    return await session.scalar(
        select(Race).where(Race.id == race_id)
    )


async def race_create(
        session: AsyncSession,
        race_in: RaceBase,
):
    race = Race(**race_in.model_dump())
    session.add(race)
    await session.commit()
    await session.refresh(race)
    return race


async def race_update(
        session: AsyncSession,
        race_update: RaceBase,
        race: Race
):
    for name, value in race_update.model_dump(exclude_unset=True).items():
        setattr(race, name, value)
    await session.commit()
    return race


async def race_delete(
        session: AsyncSession,
        race: Race
):
    await session.delete(race)
    await session.commit()
