from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from kingdom.schemas.equipment.worn import (
    WornCreate,
    WornUpdate,
    SlotBase
)
from kingdom.models.equipment import Worn, Slot, Currency
from kingdom.models.general import WornTrait
from kingdom.utils.model_result import get_model_result, get_model_m2m_result


async def slot_list(session: AsyncSession):
    stmt = select(Slot).order_by(Slot.id)
    result: Result = await session.execute(stmt)
    slots = result.scalars().all()
    return list(slots)


async def slot_create(
        session: AsyncSession,
        slot_in: SlotBase,
):
    slot = Slot(**slot_in.model_dump())
    session.add(slot)
    await session.commit()
    await session.refresh(slot)
    return slot


async def slot_update(
        session: AsyncSession,
        slot_update: SlotBase,
        slot: Slot
):
    for key, value in slot_update.model_dump(exclude_unset=True).items():
        setattr(slot, key, value)
        await session.commit()
    return slot


async def slot_delete(
        session: AsyncSession,
        slot: Slot
) -> None:
    await session.delete(slot)
    await session.commit()


async def worn_item_list(session: AsyncSession):
    stmt = select(Worn).options(
        selectinload(Worn.currency),
        selectinload(Worn.slot),
        selectinload(Worn.worn_traits)
    ).order_by(Worn.id)
    result: Result = await session.execute(stmt)
    worns = result.scalars().all()
    return list(worns)


async def worn_detail(session: AsyncSession, worn_id: int) -> Worn | None:
    return await session.scalar(
        select(Worn)
        .where(Worn.id == worn_id)
        .options(
            selectinload(Worn.currency),
            selectinload(Worn.slot),
            selectinload(Worn.worn_traits),
        )
    )


async def worn_create(session: AsyncSession, worn_in: WornCreate) -> Worn:
    slot = await get_model_result(model=Slot, object_id=worn_in.slot_id, session=session)
    currency = await get_model_result(model=Currency, object_id=worn_in.currency_id, session=session)
    worn_traits = await get_model_m2m_result(model=WornTrait, object_list=worn_in.worn_traits, session=session)

    worn = Worn(
        name=worn_in.name,
        description=worn_in.description,
        price=worn_in.price,
        weight=worn_in.weight,
        level=worn_in.level,
        activate=worn_in.activate,
        effect=worn_in.effect,
        worn_traits=worn_traits,
        slot=slot,
        currency=currency
    )
    session.add(worn)
    await session.commit()
    await session.refresh(worn)
    return await worn_detail(session, worn.id)


async def worn_update(
        worn_update: WornUpdate,
        worn: Worn,
        session: AsyncSession,
) -> Worn:
    slot = await get_model_result(model=Slot, object_id=worn_update.slot_id, session=session)
    currency = await get_model_result(model=Currency, object_id=worn_update.currency_id, session=session)
    worn_traits = await get_model_m2m_result(model=WornTrait, object_list=worn_update.worn_traits, session=session)

    for key, value in worn_update.model_dump(exclude_unset=True).items():
        if hasattr(worn, key) and key not in ["slot_id", "currency_id", "worn_traits"]:
            setattr(worn, key, value)

    worn.slot = slot
    worn.currency = currency
    worn.worn_traits.clear()
    for value in worn_traits:
        worn.worn_traits.append(value)

    await session.commit()
    await session.refresh(worn)
    return worn


async def worn_delete(worn: Worn, session: AsyncSession) -> None:
    await session.delete(worn)
    await session.commit()
