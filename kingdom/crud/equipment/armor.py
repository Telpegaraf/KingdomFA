from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from kingdom.utils.model_result import get_model_m2m_result, get_model_result
from kingdom.schemas.equipment.armor import (
    ArmorGroupBase,
    ArmorCreate,
    ArmorUpdate
)

from kingdom.models.equipment import (
    Armor,
    ArmorGroup,
    Currency
)

from kingdom.models.general import (
    ArmorTrait,
    ArmorSpecialization
)


async def armor_group_list(session: AsyncSession):
    stmt = select(ArmorGroup).order_by(ArmorGroup.id)
    result: Result = await session.execute(stmt)
    armor_groups = result.scalars().all()
    return list(armor_groups)


async def armor_group_create(
        session: AsyncSession,
        armor_group_in: ArmorGroupBase
):
    armor_group = ArmorGroup(**armor_group_in.model_dump())
    session.add(armor_group)
    await session.commit()
    await session.refresh(armor_group)
    return armor_group


async def armor_group_update(
        session: AsyncSession,
        armor_group_update: ArmorGroupBase,
        armor_group: ArmorGroup
):
    for name, value in armor_group_update.model_dump(exclude_unset=True).items():
        setattr(armor_group, name, value)
    await session.commit()
    return armor_group


async def armor_group_delete(
        armor_group: ArmorGroup,
        session: AsyncSession
):
    await session.delete(armor_group)
    await session.commit()


async def armor_list(session: AsyncSession):
    stmt = select(Armor).options(
        selectinload(Armor.armor_group),
        selectinload(Armor.armor_traits),
        selectinload(Armor.armor_specializations),
        selectinload(Armor.currency)
    ).order_by(Armor.id)
    result: Result = await session.execute(stmt)
    armors = result.scalars().all()
    return list(armors)


async def armor_detail(session: AsyncSession, armor_id: int) -> Armor | None:
    return await session.scalar(
        select(Armor)
        .where(Armor.id == armor_id)
        .options(selectinload(Armor.armor_group),
                 selectinload(Armor.armor_traits),
                 selectinload(Armor.armor_specializations),
                 selectinload(Armor.currency))
    )


async def armor_create(session: AsyncSession, armor_in: ArmorCreate) -> Armor:
    armor_group = await get_model_result(model=Armor, object_id=armor_in.armor_group_id, session=session)
    currency = await get_model_result(model=Currency, object_id=armor_in.currency_id, session=session)
    existing_armor_traits = await get_model_m2m_result(model=ArmorTrait, object_list=armor_in.armor_traits, session=session)
    existing_armor_specializations = await get_model_m2m_result(model=ArmorSpecialization,
                                                          object_list=armor_in.armor_specializations, session=session)
    armor = Armor(
        name=armor_in.name,
        description=armor_in.description,
        price=armor_in.price,
        weight=armor_in.weight,
        level=armor_in.level,
        armor_traits=existing_armor_traits,
        strength=armor_in.strength,
        check_penalty=armor_in.check_penalty,
        speed_penalty=armor_in.speed_penalty,
        ac_bonus=armor_in.ac_bonus,
        dexterity_modifier_cap=armor_in.dexterity_modifier_cap,
        category=armor_in.category,
        armor_specializations=existing_armor_specializations,
        armor_group=armor_group,
        currency=currency
    )
    session.add(armor)
    await session.commit()
    await session.refresh(armor)
    return await armor_detail(session=session, armor_id=armor.id)


async def armor_update(
        session: AsyncSession,
        armor_update: ArmorUpdate,
        armor: Armor
):
    armor_group = await get_model_result(model=Armor, object_id=armor_update.armor_group_id, session=session)
    currency = await get_model_result(model=Currency, object_id=armor_update.currency_id, session=session)
    existing_armor_traits = await get_model_m2m_result(
        model=ArmorTrait, object_list=armor_update.armor_traits, session=session
    )
    existing_armor_specializations = await get_model_m2m_result(
        model=ArmorSpecialization, object_list=armor_update.armor_specializations, session=session
    )
    for key, value in armor_update.model_dump(exclude_unset=True).items():
        if hasattr(armor, key) and key not in [
            "armor_traits", "armor_specializations", "currency_id", "armor_group_id"
        ]:
            setattr(armor, key, value)

    armor.armor_group = armor_group
    armor.currency = currency
    armor.armor_traits.clear()
    armor.armor_specializations.clear()
    for value in existing_armor_traits:
        armor.armor_traits.append(value)
    for value in existing_armor_specializations:
        armor.armor_specializations.append(value)
    await session.commit()
    await session.refresh(armor)
    return armor


async def armor_delete(
        session: AsyncSession,
        armor: Armor
):
    await session.delete(armor)
    await session.commit()
