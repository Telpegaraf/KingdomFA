from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.schemas.character.character_stats import CharacterStatsCreate, CharacterStatsUpdate
from core.models.character import CharacterStat, Character
from api_v1.utils.model_result import get_model_result


async def character_stats_detail(session: AsyncSession, character_stat_id: int) -> CharacterStat:
    return await session.scalar(
        select(CharacterStat).
        where(CharacterStat.id == character_stat_id).options(
            selectinload(CharacterStat.character),
        )
    )


async def character_stats_list(session: AsyncSession) -> list[CharacterStat]:
    stmt = select(CharacterStat).options(
        selectinload(CharacterStat.character),
    ).order_by(CharacterStat.id)
    result: Result = await session.execute(stmt)
    characters = result.scalars().all()
    return list(characters)


async def character_stats_create(
        session: AsyncSession,
        character_stats_in: CharacterStatsCreate,
) -> CharacterStat:
    character = await get_model_result(model=Character, object_id=character_stats_in.character_id, session=session)
    character_stat_data = character_stats_in.dict(exclude={"character_id"})
    character_stat = CharacterStat(
        **character_stat_data,
        character=character
    )
    session.add(character_stat)
    await session.commit()
    await session.refresh(character_stat)
    return await character_stats_detail(session=session, character_stat_id=character_stat.id)


async def character__stats_update(
        session: AsyncSession,
        character_stats_update: CharacterStatsUpdate,
        character_stat: CharacterStat
) -> CharacterStat:
    character = await get_model_result(model=Character, object_id=character_stats_update.character_id, session=session)
    for key, value in character_stats_update.model_dump(exclude_unset=True).items():
        if hasattr(character_stat, key) and key not in [
            "character_id"
        ]:
            setattr(character_stat, key, value)
    character_stat.character = character
    await session.commit()
    await session.refresh(character_stat)
    return character_stat


async def character_stat_delete(
        session: AsyncSession,
        character: CharacterStat
) -> None:
    await session.delete(character)
    await session.commit()
