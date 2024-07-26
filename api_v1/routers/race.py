from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.models.race import Race
from api_v1.schemas import race as schemas
from api_v1.crud import race as crud
from api_v1.dependencies.race import get_race
from database import db_helper


http_bearer = HTTPBearer()

race_router = APIRouter(prefix="/race", tags=["Race"])


@race_router.get(
    "/{race_id}/",
    description="Return the race object, depending on ID",
    response_model=schemas.RaceBase
)
async def race_detail(race: Race = Depends(get_race)) -> Race:
    return race


@race_router.get(
    "/",
    description="Return all race objects",
    response_model=list[schemas.Race]
)
async def race_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[Race]:
    return await crud.race_list(session=session)


@race_router.post(
    "/create/",
    description="Create a new race object",
    response_model=schemas.RaceBase,
    status_code=status.HTTP_201_CREATED
)
async def race_create(
        race_in: schemas.RaceBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Race:
    return await crud.race_create(session=session, race_in=race_in)


@race_router.patch(
    "/update/{race_id}/",
    description="Update the race object, depending on ID",
    response_model=schemas.RaceBase
)
async def race_update(
        race_update: schemas.RaceBase,
        race: Race = Depends(get_race),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Race:
    return await crud.race_update(session=session, race=race, race_update=race_update)


@race_router.delete(
    "/delete/{race_id}/",
    description="Delete the race object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def race_delete(
        race: Race = Depends(get_race),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.race_delete(session=session, race=race)
