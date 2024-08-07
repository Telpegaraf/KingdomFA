from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from kingdom.schemas.character.character_points import CharacterPointCreate, CharacterPointUpdate
from kingdom.models.character import CharacterPoint, Character
from kingdom.utils.model_result import get_model_result


async def character_point_detail(session: AsyncSession, character_point_id: int) -> CharacterPoint:
    return await session.scalar(
        select(CharacterPoint).
        where(CharacterPoint.id == character_point_id).options(
            selectinload(CharacterPoint.character),
        )
    )


async def character_point_list(session: AsyncSession) -> list[CharacterPoint]:
    stmt = select(CharacterPoint).options(
        selectinload(CharacterPoint.character),
    ).order_by(CharacterPoint.id)
    result: Result = await session.execute(stmt)
    characters = result.scalars().all()
    return list(characters)


async def character_point_create(
        session: AsyncSession,
        character_point_in: CharacterPointCreate,
) -> CharacterPoint:
    character = await get_model_result(model=Character, object_id=character_point_in.character_id, session=session)
    character_point_data = character_point_in.dict(exclude={"character_id"})
    character_point = CharacterPoint(
        **character_point_data,
        character=character
    )
    session.add(character_point)
    await session.commit()
    await session.refresh(character_point)
    return await character_point_detail(session=session, character_point_id=character_point.id)


async def character_stats_update(
        session: AsyncSession,
        character_point_update: CharacterPointUpdate,
        character_point: CharacterPoint
) -> CharacterPoint:
    character = await get_model_result(model=Character, object_id=character_point_update.character_id, session=session)
    for key, value in character_point_update.model_dump(exclude_unset=True).items():
        if hasattr(character_point, key) and key not in [
            "character_id"
        ]:
            setattr(character_point, key, value)
    character_point.character = character
    await session.commit()
    await session.refresh(character_point)
    return character_point


async def character_point_delete(
        session: AsyncSession,
        character: CharacterPoint
) -> None:
    await session.delete(character)
    await session.commit()
