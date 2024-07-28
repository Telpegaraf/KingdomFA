from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.schemas.character.character_stats import CharacterStatsCreate, CharacterStatsUpdate
from api_v1.models.character import CharacterStat
from api_v1.models.user import User
from api_v1.models.religion import God, Domain
from api_v1.models.race import Race
from api_v1.models.character_class import CharacterClass
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
    character = await get_model_result(model=User, object_id=character_stats_in.character_id, session=session)
    character_stat = CharacterStat(
        strength = character_stats_in.strength,
        dexterity = character_stats_in.dexterity,
        constitution = character_stats_in.constitution,
        intelligence = character_stats_in.intelligence,
        wisdom = character_stats_in.wisdom,
        charisma = character_stats_in.charisma,
        max_speed = character_stats_in.max_speed,
        speed = character_stats_in.speed,
        perception_mastery = character_stats_in.perception_mastery,
        unarmed_mastery = character_stats_in.unarmed_mastery,
        light_armor_mastery = character_stats_in.light_armor_mastery,
        medium_armor_mastery = character_stats_in.medium_armor_mastery,
        heavy_armor_mastery = character_stats_in.heavy_armor_mastery,
        fortitude_mastery = character_stats_in.fortitude_mastery,
        reflex_armor_mastery = character_stats_in.reflex_armor_mastery,
        will_armor_mastery = character_stats_in.will_armor_mastery,
        character=character
    )
    session.add(character_stat)
    await session.commit()
    await session.refresh(character_stat)
    return await character_stats_detail(session=session, character_stat_id=character_stat.id)


async def character_update(
        session: AsyncSession,
        character_stats_update: CharacterStatsUpdate,
        character_stat: CharacterStat
) -> CharacterStat:
    character = await get_model_result(model=User, object_id=character_stats_update.character_id, session=session)
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
