from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from kingdom.crud.character.character import character_detail
from kingdom.models.character import Character


async def get_character(
        character_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> Character | None:
    return await character_detail(session=session, character_id=character_id)
