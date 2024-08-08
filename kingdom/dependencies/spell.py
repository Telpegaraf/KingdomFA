from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from kingdom.crud.spell import spell_detail
from kingdom.models.spell import Spell


async def get_spell(
        spell_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> Spell | None:
    return await spell_detail(session=session, spell_id=spell_id)
