from fastapi import Path, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from api_v1.crud.god import god_detail
from api_v1.models.god import God
from database import db_helper



async def get_god_by_id(
        god_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> God:
    god = await god_detail(god_id=god_id, session=session)
    if god is not None:
        return god
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"God {god_id} isn't found",
    )
