from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.schemas.equipment.worn import (
    WornBase,
    WornCreate
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

# async def worn_create(session: AsyncSession, worn_in: WornBase) -> Worn:
#     worn_traits_name = [worn_trait.name for worn_trait in worn_in.worn_traits]
#     existing_worn_traits = await session.execute(
#         select(WornTrait).where(WornTrait.name.in_(worn_traits_name))
#     )
#     existing_worn_traits = existing_worn_traits.scalars().all()
#     existing_worn_trait_dict = {worn_trait.name: worn_trait for worn_trait in existing_worn_traits}
#     worn_traits = []
#     for worn_trait_in in worn_in.worn_traits:
#         if worn_trait_in.name in existing_worn_trait_dict:
#             worn_traits.append(existing_worn_trait_dict[worn_trait_in.name])
#         else:
#             new_worn_trait = WornTrait(name=worn_trait_in.name)
#             session.add(new_worn_trait)
#             await session.flush()
#             worn_traits.append(new_worn_trait)
#
#     try:
#         existing_slot = await session.execute(
#             select(Slot).where(Slot.slot == worn_in.slot.slot)
#         )
#         slot = existing_slot.scalar_one()
#     except NoResultFound:
#         slot = Slot(slot=worn_in.slot.slot, limit=worn_in.slot.limit)
#         session.add(slot)
#         await session.flush()
#
#     try:
#         existing_currency = await session.execute(
#             select(Currency).where(Currency.name == worn_in.currency.name)
#         )
#         currency = existing_currency.scalar_one()
#     except NoResultFound:
#         currency = Currency(name=worn_in.currency.name, price=worn_in.currency.price,
#                             description=worn_in.currency.description, weight=worn_in.currency.weight)
#         session.add(currency)
#         await session.flush()
#
#     worn = Worn(
#         name=worn_in.name,
#         description=worn_in.description,
#         price=worn_in.price,
#         weight=worn_in.weight,
#         level=worn_in.level,
#         activate=worn_in.activate,
#         effect=worn_in.effect,
#         worn_traits=worn_traits,
#         slot=slot,
#         currency=currency
#     )
#     session.add(worn)
#     await session.commit()
#     await session.refresh(worn)
#     return worn


async def worn_update(
        worn_update: WornBase,
        worn: Worn,
        session: AsyncSession,
) -> Worn:
    for name, value in worn_update.model_dump(exclude_unset=True).items():
        setattr(worn, name, value)
    await session.commit()
    return worn


async def worn_delete(worn: Worn, session: AsyncSession) -> None:
    await session.delete(worn)
    await session.commit()
