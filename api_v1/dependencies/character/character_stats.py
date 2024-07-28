from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.crud.character.character_stats import character_stats_detail
from api_v1.models.character import CharacterStat


async def get_character_stats(
        character_stats_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterStat | None:
    return await character_stats_detail(session=session, character_id=character_stats_id)
