from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from kingdom.utils.model_result import get_model_result
from kingdom.schemas.equipment.item import (
    ItemCreateUpdate,
)

from kingdom.models.equipment import (
    Item,
    Currency
)


async def item_list(session: AsyncSession):
    stmt = select(Item).options(
        selectinload(Item.currency)
    ).order_by(Item.id)
    result: Result = await session.execute(stmt)
    armors = result.scalars().all()
    return list(armors)


async def item_detail(session: AsyncSession, item_id: int) -> Item | None:
    return await session.scalar(
        select(Item)
        .where(Item.id == item_id)
        .options(selectinload(Item.currency))
    )


async def item_create(session: AsyncSession, item_in: ItemCreateUpdate) -> Item:
    currency = await get_model_result(model=Currency, object_id=item_in.currency_id, session=session)
    item_data = item_in.dict(exclude={"currency"})
    armor = Item(
        **item_data,
        currency=currency
    )
    session.add(armor)
    await session.commit()
    await session.refresh(armor)
    return await item_detail(session=session, item_id=armor.id)


async def item_update(
        session: AsyncSession,
        item_update: ItemCreateUpdate,
        item: Item
):
    currency = await get_model_result(model=Currency, object_id=item_update.currency_id, session=session)
    for key, value in item_update.model_dump(exclude_unset=True).items():
        if hasattr(item, key) and key not in [
            "currency_id"
        ]:
            setattr(item, key, value)
    item.currency = currency
    await session.commit()
    await session.refresh(item)
    return item


async def item_delete(
        session: AsyncSession,
        item: Item
):
    await session.delete(item)
    await session.commit()
