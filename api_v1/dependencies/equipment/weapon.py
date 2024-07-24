from annotated_types import Annotated
from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.crud.equipment.weapon import weapon_detail
from api_v1.models.equipment import Weapon


async def get_weapon(
        weapon_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> Weapon | None:
    return await weapon_detail(
        session=session, weapon_id=weapon_id
    )
