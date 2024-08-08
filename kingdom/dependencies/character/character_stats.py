from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from kingdom.crud.character.character_stats import character_stats_detail
from kingdom.models.character import CharacterStat


async def get_character_stats(
        character_stat_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterStat | None:
    return await character_stats_detail(session=session, character_stat_id=character_stat_id)
