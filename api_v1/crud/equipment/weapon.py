from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.models.equipment import Weapon, Currency
from api_v1.models.general import DamageType, WeaponGroup, WeaponSpecialization, WeaponTrait
from api_v1.schemas.equipment.weapon import WeaponCreate, WeaponUpdate


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
    weapon_group_result = await session.execute(
        select(WeaponGroup).where(WeaponGroup.id == weapon_in.weapon_group_id)
    )
    weapon_group = weapon_group_result.scalar_one_or_none()
    if weapon_group is None:
        raise HTTPException(status_code=404, detail="Weapon Group is not found")

    currency_result = await session.execute(
        select(Currency).where(Currency.id == weapon_in.currency_id)
    )
    currency = currency_result.scalar_one_or_none()
    if currency is None:
        raise HTTPException(status_code=404, detail="Currency is not found")

    specialization_result = await session.execute(
        select(WeaponSpecialization).where(WeaponSpecialization.id == weapon_in.weapon_specialization_id)
    )
    specialization = specialization_result.scalar_one_or_none()
    if specialization is None:
        raise HTTPException(status_code=404, detail="Specialization is not found")

    damage_type_result = await session.execute(
        select(DamageType).where(DamageType.id == weapon_in.damage_type_id)
    )
    damage_type = damage_type_result.scalar_one_or_none()
    if damage_type is None:
        raise HTTPException(status_code=404, detail="Damage type is not found")
    print(damage_type)

    second_damage_type_result = await session.execute(
        select(DamageType).where(DamageType.id == weapon_in.second_damage_type_id)
    )
    second_damage_type = second_damage_type_result.scalar_one_or_none()
    if second_damage_type is None:
        raise HTTPException(status_code=404, detail="Damage type is not found")

    weapon_traits_result = await session.execute(
        select(WeaponTrait).where(WeaponTrait.id.in_(weapon_in.weapon_traits))
    )
    existing_weapon_traits = weapon_traits_result.scalars().all()

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
        weapon_traits=existing_weapon_traits,
        currency=currency
    )
    session.add(weapon)
    await session.commit()
    await session.refresh(weapon)
    return weapon


async def weapon_update(
        session: AsyncSession,
        weapon_update: WeaponUpdate,
        weapon: Weapon
):
    pass


async def weapon_delete(session: AsyncSession, weapon: Weapon):
    await session.delete(weapon)
    await session.commit()
