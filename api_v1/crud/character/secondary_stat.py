from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.schemas.character.secondary_stat import SecondaryStatCreate, SecondaryStatUpdate
from api_v1.models.character import SecondaryStat, Character
from api_v1.utils.model_result import get_model_result


async def secondary_stat_detail(session: AsyncSession, secondary_stat_id: int) -> SecondaryStat:
    return await session.scalar(
        select(SecondaryStat).
        where(SecondaryStat.id == secondary_stat_id).options(
            selectinload(SecondaryStat.character),
        )
    )


async def secondary_stat_list(session: AsyncSession) -> list[SecondaryStat]:
    stmt = select(SecondaryStat).options(
        selectinload(SecondaryStat.character),
    ).order_by(SecondaryStat.id)
    result: Result = await session.execute(stmt)
    characters = result.scalars().all()
    return list(characters)


async def secondary_stat_create(
        session: AsyncSession,
        secondary_stat_in: SecondaryStatCreate,
) -> SecondaryStat:
    character = await get_model_result(model=Character, object_id=secondary_stat_in.character_id, session=session)
    secondary_stat = SecondaryStat(
        perception=secondary_stat_in.perception,
        armor_class=secondary_stat_in.armor_class,
        attack_class=secondary_stat_in.attack_class,
        damage_bonus=secondary_stat_in.damage_bonus,
        max_health=secondary_stat_in.max_health,
        health=secondary_stat_in.health,
        initiative=secondary_stat_in.initiative,
        fortitude_saving=secondary_stat_in.fortitude_saving,
        reflex_saving=secondary_stat_in.reflex_saving,
        will_saving=secondary_stat_in.will_saving,
        character=character
    )
    session.add(secondary_stat)
    await session.commit()
    await session.refresh(secondary_stat)
    return await secondary_stat_detail(session=session, secondary_stat_id=secondary_stat.id)


async def secondary_stat_update(
        session: AsyncSession,
        secondary_stat_update: SecondaryStatUpdate,
        secondary_stat: SecondaryStat
) -> SecondaryStat:
    character = await get_model_result(model=Character, object_id=secondary_stat_update.character_id, session=session)
    for key, value in secondary_stat_update.model_dump(exclude_unset=True).items():
        if hasattr(secondary_stat, key) and key not in [
            "character_id"
        ]:
            setattr(secondary_stat, key, value)
    secondary_stat.character = character
    await session.commit()
    await session.refresh(secondary_stat)
    return secondary_stat


async def secondary_stat_delete(
        session: AsyncSession,
        character: SecondaryStat
) -> None:
    await session.delete(character)
    await session.commit()
