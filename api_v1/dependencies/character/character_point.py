from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.crud.character.character_points import character_point_detail
from api_v1.models.character import CharacterPoint


async def get_character_point(
        character_point_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterPoint | None:
    return await character_point_detail(session=session, character_point_id=character_point_id)
