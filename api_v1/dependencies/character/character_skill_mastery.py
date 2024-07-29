from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.crud.character.character_skill_mastery import character_skill_mastery_detail
from api_v1.models.character import CharacterSkillMastery


async def get_character_skill_mastery(
        character_skill_mastery_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterSkillMastery | None:
    return await character_skill_mastery_detail(session=session, character_skill_mastery_id=character_skill_mastery_id)
