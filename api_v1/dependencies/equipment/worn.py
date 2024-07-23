from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

import database
from api_v1.crud.equipment.worn import worn_detail
from api_v1.models.equipment import Worn


async def get_worn(
    worn_id: Annotated[int, Path],
    session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> Worn:
    return await worn_detail(session=session, worn_id=worn_id)
