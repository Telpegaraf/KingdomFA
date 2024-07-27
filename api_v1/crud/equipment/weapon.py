from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.models.equipment import Weapon, Currency
from api_v1.models.general import DamageType, WeaponGroup, WeaponSpecialization, WeaponTrait
from api_v1.schemas.equipment.weapon import WeaponCreate, WeaponUpdate
from api_v1.utils.model_result import get_model_m2m_result, get_model_result


async def weapon_detail(session: AsyncSession, weapon_id: int) -> Weapon | None:
    return await session.scalar(
        select(Weapon)
        .where(Weapon.id == weapon_id)
        .options(
            selectinload(Weapon.damage_type),
            selectinload(Weapon.second_damage_type),
            selectinload(Weapon.weapon_group),
            selectinload(Weapon.weapon_specialization),
            selectinload(Weapon.weapon_traits),
            selectinload(Weapon.currency)
        )
    )


async def weapon_list(session: AsyncSession) -> list[Weapon]:
    stmt = select(Weapon).options(
        selectinload(Weapon.damage_type),
        selectinload(Weapon.second_damage_type),
        selectinload(Weapon.weapon_group),
        selectinload(Weapon.weapon_specialization),
        selectinload(Weapon.weapon_traits),
        selectinload(Weapon.currency)
    ).order_by(Weapon.id)
    result: Result = await session.execute(stmt)
    weapons = result.scalars().all()
    return list(weapons)


async def weapon_create(
        session: AsyncSession,
        weapon_in: WeaponCreate,
) -> Weapon:
    weapon_group = await get_model_result(model=WeaponGroup, object_id=weapon_in.weapon_group_id, session=session)
    currency = await get_model_result(model=Currency, object_id=weapon_in.currency_id, session=session)
    specialization = await get_model_result(model=WeaponSpecialization,
                                      object_id=weapon_in.weapon_specialization_id, session=session)
    await get_model_result(model=DamageType, object_id=weapon_in.damage_type_id, session=session)
    if weapon_in.second_damage_type_id:
        await get_model_result(model=DamageType, object_id=weapon_in.second_damage_type_id, session=session)
    weapon_traits = await get_model_m2m_result(model=WeaponTrait, object_list=weapon_in.weapon_traits, session=session)

    weapon = Weapon(
        name=weapon_in.name,
        description=weapon_in.description,
        price=weapon_in.price,
        weight=weapon_in.weight,
        level=weapon_in.level,
        two_hands=weapon_in.two_hands,
        range=weapon_in.range,
        reload=weapon_in.reload,
        damage_type_id=weapon_in.damage_type_id,
        second_damage_type_id=weapon_in.second_damage_type_id,
        weapon_group=weapon_group,
        weapon_specialization=specialization,
        dice=weapon_in.dice,
        dice_count=weapon_in.dice_count,
        bonus_damage=weapon_in.bonus_damage,
        second_dice=weapon_in.second_dice,
        second_dice_count=weapon_in.second_dice_count,
        second_bonus_damage=weapon_in.second_bonus_damage,
        weapon_traits=weapon_traits,
        currency=currency
    )
    session.add(weapon)
    await session.commit()
    await session.refresh(weapon)
    return await weapon_detail(session=session, weapon_id=weapon.id)


async def weapon_update(
        session: AsyncSession,
        weapon_update: WeaponUpdate,
        weapon: Weapon
):
    weapon_group = await get_model_result(model=WeaponGroup, object_id=weapon_update.weapon_group_id, session=session)
    currency = await get_model_result(model=Currency, object_id=weapon_update.currency_id, session=session)
    specialization = await get_model_result(model=WeaponSpecialization,
                                            object_id=weapon_update.weapon_specialization_id, session=session)
    await get_model_result(model=DamageType, object_id=weapon_update.damage_type_id, session=session)
    if weapon_update.second_damage_type_id:
        await get_model_result(model=DamageType, object_id=weapon_update.second_damage_type_id, session=session)
    weapon_traits = await get_model_m2m_result(model=WeaponTrait,
                                               object_list=weapon_update.weapon_traits, session=session)

    for key, value in weapon_update.model_dump(exclude_unset=True).items():
        if hasattr(weapon, key) and key not in [
            "weapon_traits", "weapon_specializations", "currency_id",
            "weapon_group_id", "damage_type_id", "second_damage_type_id"
        ]:
            setattr(weapon, key, value)

    weapon.weapon_group = weapon_group
    weapon.weapon_specialization = specialization
    weapon.currency = currency
    weapon.damage_type_id = weapon_update.damage_type_id
    weapon.second_damage_type_id = weapon_update.second_damage_type_id
    weapon.weapon_traits.clear()
    for value in weapon_traits:
        weapon.weapon_traits.append(value)
    await session.commit()
    await session.refresh(weapon)
    return weapon


async def weapon_delete(session: AsyncSession, weapon: Weapon):
    await session.delete(weapon)
    await session.commit()
