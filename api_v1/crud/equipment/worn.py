from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.schemas.equipment.worn import (
    WornCreate,
    WornUpdate,
)
from api_v1.models.equipment import Worn, Slot, Currency
from api_v1.models.general import WornTrait


async def worn_item_list(session: AsyncSession):
    stmt = select(Worn).order_by(Worn.id)
    result: Result = await session.execute(stmt)
    worns = result.scalars().all()
    return list(worns)


async def worn_detail(session: AsyncSession, worn_id: int) -> Worn | None:
    return await session.get(Worn, worn_id)


async def worn_create(session: AsyncSession, worn_in: WornCreate) -> Worn:
    slot_result = await session.execute(
        select(Slot).where(Slot.id == worn_in.slot_id)
    )
    slot = slot_result.scalar_one_or_none()
    if slot is None:
        raise HTTPException(status_code=404, detail="Slot not found")

    currency_result = await session.execute(
        select(Currency).where(Currency.id == worn_in.currency_id)
    )
    currency = currency_result.scalar_one_or_none()
    if currency is None:
        raise HTTPException(status_code=404, detail="currency not found")

    worn_traits_result = await session.execute(
        select(WornTrait).where(WornTrait.id.in_(worn_in.worn_traits))
    )
    existing_worn_traits = worn_traits_result.scalars().all()

    worn = Worn(
        name=worn_in.name,
        description=worn_in.description,
        price=worn_in.price,
        weight=worn_in.weight,
        level=worn_in.level,
        activate=worn_in.activate,
        effect=worn_in.effect,
        worn_traits=existing_worn_traits,
        slot=slot,
        currency=currency
    )
    session.add(worn)
    await session.commit()
    await session.refresh(worn)
    return worn


async def worn_update(
        worn_update: WornUpdate,
        worn: Worn,
        session: AsyncSession,
) -> Worn:
    slot_result = await session.execute(
        select(Slot).where(Slot.id == worn_update.slot_id)
    )
    slot = slot_result.scalar_one_or_none()
    if slot is None:
        raise HTTPException(status_code=404, detail="Slot not found")

    currency_result = await session.execute(
        select(Currency).where(Currency.id == worn_update.currency_id)
    )
    currency = currency_result.scalar_one_or_none()
    if currency is None:
        raise HTTPException(status_code=404, detail="currency not found")

    for key, value in worn_update.model_dump(exclude_unset=True).items():
        if hasattr(worn, key) and key not in ["slot_id", "currency_id", "worn_traits"]:
            print(key)
            setattr(worn, key, value)

    await session.commit()
    await session.refresh(worn)
    return worn


async def worn_delete(worn: Worn, session: AsyncSession) -> None:
    await session.delete(worn)
    await session.commit()
