from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from kingdom.schemas.character.character_weapon_mastery import(
    CharacterWeaponMasteryCreate,
    CharacterWeaponMasteryUpdate
)
from kingdom.models.character import CharacterWeaponMastery, Character
from kingdom.models.general import WeaponGroup
from kingdom.utils.model_result import get_model_result


async def character_weapon_mastery_detail(
        session: AsyncSession,
        character_weapon_mastery_id: int
) -> CharacterWeaponMastery:
    return await session.scalar(
        select(CharacterWeaponMastery).
        where(CharacterWeaponMastery.id == character_weapon_mastery_id).options(
            selectinload(CharacterWeaponMastery.character),
            selectinload(CharacterWeaponMastery.weapon_group)
        )
    )


async def character_weapon_mastery_list(session: AsyncSession) -> list[CharacterWeaponMastery]:
    stmt = select(CharacterWeaponMastery).options(
        selectinload(CharacterWeaponMastery.character),
        selectinload(CharacterWeaponMastery.weapon_group)
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
    weapon_group = await get_model_result(
        model=WeaponGroup,
        object_id=character_weapon_mastery_in.weapon_group_id,
        session=session
    )
    character_weapon_mastery = CharacterWeaponMastery(
        mastery_level=character_weapon_mastery_in.mastery_level,
        weapon_group=weapon_group,
        character=character
    )
    session.add(character_weapon_mastery)
    await session.commit()
    await session.refresh(character_weapon_mastery)
    return await character_weapon_mastery_detail(
        session=session,
        character_weapon_mastery_id=character_weapon_mastery.id
    )


async def character_weapon_mastery_update(
        session: AsyncSession,
        character_weapon_mastery_update: CharacterWeaponMasteryUpdate,
        character_weapon_mastery: CharacterWeaponMastery
) -> CharacterWeaponMastery:
    character = await get_model_result(
        model=Character,
        object_id=character_weapon_mastery_update.character_id,
        session=session
    )
    weapon_group = await get_model_result(
        model=WeaponGroup,
        object_id=character_weapon_mastery_update.weapon_group_id,
        session=session
    )
    for key, value in character_weapon_mastery_update.model_dump(exclude_unset=True).items():
        if hasattr(character_weapon_mastery, key) and key not in [
            "character_id", "weapon_group_id"
        ]:
            setattr(character_weapon_mastery, key, value)
    character_weapon_mastery.character = character
    character_weapon_mastery.weapon_group = weapon_group
    await session.commit()
    await session.refresh(character_weapon_mastery)
    return character_weapon_mastery


async def character_weapon_mastery_delete(
        session: AsyncSession,
        character: CharacterWeaponMastery
) -> None:
    await session.delete(character)
    await session.commit()
