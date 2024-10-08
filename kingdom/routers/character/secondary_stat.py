from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from kingdom.models.character import SecondaryStat
from kingdom.schemas.character import secondary_stat as schemas
from kingdom.crud.character import secondary_stat as crud
from kingdom.dependencies.character.secondary_stat import get_secondary_stat
from database import db_helper


http_bearer = HTTPBearer()

secondary_stat_router = APIRouter(prefix="/secondary_stat", tags=["Secondary Stat"])


@secondary_stat_router.get(
    "/{secondary_stat_id}/",
    description="Return the Secondary Stat object, depending on ID",
    response_model=schemas.SecondaryStatRead
)
async def secondary_stat_detail(character: SecondaryStat = Depends(get_secondary_stat)) -> SecondaryStat:
    return character


@secondary_stat_router.get(
    "/",
    description="Return all Secondary Stat objects",
    response_model=list[schemas.SecondaryStat]
)
async def secondary_stat_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[SecondaryStat]:
    return await crud.secondary_stat_list(session=session)


@secondary_stat_router.post(
    "/",
    description="Create a new Secondary Stat object",
    response_model=schemas.SecondaryStatRead,
    status_code=status.HTTP_201_CREATED
)
async def secondary_stat_create(
        secondary_stat_in: schemas.SecondaryStatCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> SecondaryStat:
    return await crud.secondary_stat_create(session=session, secondary_stat_in=secondary_stat_in)


@secondary_stat_router.patch(
    "/{secondary_stat_id}/",
    description="Update the Secondary Stat object, depending on ID",
    response_model=schemas.SecondaryStatRead
)
async def secondary_stat_update(
        secondary_stat_update: schemas.SecondaryStatUpdate,
        secondary_stat: SecondaryStat = Depends(get_secondary_stat),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> SecondaryStat:
    return await crud.secondary_stat_update(session=session, secondary_stat=secondary_stat,
                                              secondary_stat_update=secondary_stat_update)


@secondary_stat_router.delete(
    "/{secondary_stat_id}/",
    description="Delete the Secondary Stat object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def secondary_stat_delete(
        character: SecondaryStat = Depends(get_secondary_stat),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.secondary_stat_delete(session=session, character=character)
