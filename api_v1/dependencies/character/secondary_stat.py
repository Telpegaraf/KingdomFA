from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.crud.character.secondary_stat import secondary_stat_detail
from core.models.character import SecondaryStat


async def get_secondary_stat(
        secondary_stat_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> SecondaryStat | None:
    return await secondary_stat_detail(session=session, secondary_stat_id=secondary_stat_id)
