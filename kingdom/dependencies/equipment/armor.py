from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

import database
from kingdom.models.equipment import Armor
from kingdom.crud.equipment.armor import armor_detail


async def get_armor(
        armor_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency),
) -> Armor | None:
    return await armor_detail(session=session, armor_id=armor_id)
