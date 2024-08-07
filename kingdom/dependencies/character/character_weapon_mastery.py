from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from kingdom.crud.character.character_weapon_mastery import character_weapon_mastery_detail
from kingdom.models.character import CharacterWeaponMastery


async def get_character_weapon_mastery(
        character_weapon_mastery_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterWeaponMastery | None:
    return await character_weapon_mastery_detail(
        session=session,
        character_weapon_mastery_id=character_weapon_mastery_id
    )
