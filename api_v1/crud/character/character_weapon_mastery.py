from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.schemas.character.character_weapon_mastery import(
    CharacterWeaponMasteryCreate,
    CharacterWeaponMasteryUpdate
)
from api_v1.models.character import CharacterWeaponMastery, Character
from api_v1.models.general import WeaponGroup
from api_v1.utils.model_result import get_model_result


async def character_weapon_mastery_detail(
        session: AsyncSession,
        character_weapon_mastery_id: int
) -> CharacterWeaponMastery:
    return await session.scalar(
        select(CharacterWeaponMastery).
        where(CharacterWeaponMastery.id == character_weapon_mastery_id).options(
            selectinload(CharacterWeaponMastery.character),
            selectinload(CharacterWeaponMastery.weapon)
        )
    )


async def character_weapon_mastery_list(session: AsyncSession) -> list[CharacterWeaponMastery]:
    stmt = select(CharacterWeaponMastery).options(
        selectinload(CharacterWeaponMastery.character),
        selectinload(CharacterWeaponMastery.weapon)
    ).order_by(CharacterWeaponMastery.id)
    result: Result = await session.execute(stmt)
    characters = result.scalars().all()
    return list(characters)


async def character_weapon_mastery_create(
        session: AsyncSession,
        character_weapon_mastery_in: CharacterWeaponMasteryCreate,
) -> CharacterWeaponMastery:
    character = await get_model_result(
        model=Character,
        object_id=character_weapon_mastery_in.character_id,
        session=session
    )
    weapon = await get_model_result(
        model=WeaponGroup,
        object_id=character_weapon_mastery_in.weapon_id,
        session=session
    )
    character_weapon_mastery = CharacterWeaponMastery(
        mastery_level=character_weapon_mastery_in.mastery_level,
        weapon=weapon,
        character=character
    )
    session.add(character_weapon_mastery)
    await session.commit()
    await session.refresh(character_weapon_mastery)
    return await character_weapon_mastery_detail(
        session=session,
        character_weapon_mastery_id=character_weapon_mastery.id
    )


async def character_stats_update(
        session: AsyncSession,
        character_weapon_mastery_update: CharacterWeaponMasteryUpdate,
        character_weapon_mastery: CharacterWeaponMastery
) -> CharacterWeaponMastery:
    character = await get_model_result(
        model=Character,
        object_id=character_weapon_mastery_update.character_id,
        session=session
    )
    weapon = await get_model_result(
        model=WeaponGroup,
        object_id=character_weapon_mastery_update.weapon_id,
        session=session
    )
    for key, value in character_weapon_mastery_update.model_dump(exclude_unset=True).items():
        if hasattr(character_weapon_mastery, key) and key not in [
            "character_id", "weapon_id"
        ]:
            setattr(character_weapon_mastery, key, value)
    character_weapon_mastery.character = character
    character_weapon_mastery.weapon = weapon
    await session.commit()
    await session.refresh(character_weapon_mastery)
    return character_weapon_mastery


async def character_weapon_mastery_delete(
        session: AsyncSession,
        character: CharacterWeaponMastery
) -> None:
    await session.delete(character)
    await session.commit()
