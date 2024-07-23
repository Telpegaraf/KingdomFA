from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.models.equipment import Weapon
from api_v1.models.general import DamageType
from api_v1.schemas.equipment.


async def weapon_detail(session: AsyncSession, weapon: Weapon) -> Weapon | None:
    return await session.scalar(
        select(Weapon)
        .where(Weapon.id == weapon.id)
        .options(
            selectinload(Weapon.damage_type),
            selectinload(Weapon.second_damage_type),
            selectinload(Weapon.weapon_group),
            selectinload(Weapon.weapon_specialization),
            selectinload(Weapon.weapon_traits)
        )
    )


async def weapon_list(session: AsyncSession) -> list[Weapon]:
    stmt = select(Weapon).options(
        selectinload(Weapon.damage_type),
        selectinload(Weapon.second_damage_type),
        selectinload(Weapon.weapon_group),
        selectinload(Weapon.weapon_specialization),
        selectinload(Weapon.weapon_traits)
    ).order_by(Weapon.id)
    result: Result = await session.execute(stmt)
    weapons = result.scalars().all()
    return list(weapons)


async def weapon_create(
        session: AsyncSession,
        weapon_in:
)


async def weapon_delete(session: AsyncSession, weapon: Weapon):
    await session.delete(weapon)
    await session.commit()
