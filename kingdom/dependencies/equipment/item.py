from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

import database
from kingdom.models.equipment import Item
from kingdom.crud.equipment.item import item_detail


async def get_item(
        item_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency),
) -> Item | None:
    return await item_detail(session=session, item_id=item_id)
