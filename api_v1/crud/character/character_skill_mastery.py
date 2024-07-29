from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.schemas.character.character_skill_mastery import CharacterSkillMasteryCreate, CharacterSkillMasteryUpdate
from api_v1.models.character import CharacterSkillMastery, Character
from api_v1.models.general import Skill
from api_v1.utils.model_result import get_model_result


async def character_skill_mastery_detail(
        session: AsyncSession,
        character_skill_mastery_id: int
) -> CharacterSkillMastery:
    return await session.scalar(
        select(CharacterSkillMastery).
        where(CharacterSkillMastery.id == character_skill_mastery_id).options(
            selectinload(CharacterSkillMastery.character),
            selectinload(CharacterSkillMastery.skill)
        )
    )


async def character_skill_mastery_list(session: AsyncSession) -> list[CharacterSkillMastery]:
    stmt = select(CharacterSkillMastery).options(
        selectinload(CharacterSkillMastery.character),
        selectinload(CharacterSkillMastery.skill)
    ).order_by(CharacterSkillMastery.id)
    result: Result = await session.execute(stmt)
    characters = result.scalars().all()
    return list(characters)


async def character_skill_mastery_create(
        session: AsyncSession,
        character_skill_mastery_in: CharacterSkillMasteryCreate,
) -> CharacterSkillMastery:
    character = await get_model_result(
        model=Character,
        object_id=character_skill_mastery_in.character_id,
        session=session
    )
    skill = await get_model_result(
        model=Skill,
        object_id=character_skill_mastery_in.skill_id,
        session=session
    )
    character_skill_mastery = CharacterSkillMastery(
        mastery_level=character_skill_mastery_in.mastery_level,
        skill=skill,
        character=character
    )
    session.add(character_skill_mastery)
    await session.commit()
    await session.refresh(character_skill_mastery)
    return await character_skill_mastery_detail(session=session, character_skill_mastery_id=character_skill_mastery.id)


async def character_stats_update(
        session: AsyncSession,
        character_skill_mastery_update: CharacterSkillMasteryUpdate,
        character_skill_mastery: CharacterSkillMastery
) -> CharacterSkillMastery:
    character = await get_model_result(
        model=Character,
        object_id=character_skill_mastery_update.character_id,
        session=session
    )
    skill = await get_model_result(
        model=Skill,
        object_id=character_skill_mastery_update.skill_id,
        session=session
    )
    for key, value in character_skill_mastery_update.model_dump(exclude_unset=True).items():
        if hasattr(character_skill_mastery, key) and key not in [
            "character_id", "skill_id"
        ]:
            setattr(character_skill_mastery, key, value)
    character_skill_mastery.character = character
    character_skill_mastery.skill = skill
    await session.commit()
    await session.refresh(character_skill_mastery)
    return character_skill_mastery


async def character_skill_mastery_delete(
        session: AsyncSession,
        character: CharacterSkillMastery
) -> None:
    await session.delete(character)
    await session.commit()
