from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.crud.race import race_detail
from core.models.race import Race


async def get_race(
        race_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> Race | None:
    return await race_detail(session=session, race_id=race_id)
