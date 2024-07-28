from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.models.character import CharacterStat
from api_v1.schemas.character import character_stats as schemas
from api_v1.crud.character import character_stats as crud
from api_v1.dependencies.character.character_stats import get_character_stats
from database import db_helper


http_bearer = HTTPBearer()

character_stats_router = APIRouter(prefix="/character_stats", tags=["Character Stats"])


@character_stats_router.get(
    "/{character_stats_id}/",
    description="Return the Character Stat object, depending on ID",
    response_model=schemas.CharacterStatsRead
)
async def character_stats_detail(character: CharacterStat = Depends(get_character_stats)) -> CharacterStat:
    return character


@character_stats_router.get(
    "/",
    description="Return all Character Stat objects",
    response_model=list[schemas.CharacterStats]
)
async def character_stats_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterStat]:
    return await crud.character_stats_list(session=session)


@character_stats_router.post(
    "/create/",
    description="Create a new Character Stat object",
    response_model=schemas.CharacterStatsRead,
    status_code=status.HTTP_201_CREATED
)
async def character_stats_create(
        character_stats_in: schemas.CharacterStatsCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterStat:
    return await crud.character_stats_create(session=session, character_stats_in=character_stats_in)


@character_stats_router.patch(
    "/update/{character_stats_id}/",
    description="Update the Character Stat object, depending on ID",
    response_model=schemas.CharacterStatsRead
)
async def character_update(
        character_stats_update: schemas.CharacterStatsUpdate,
        character_stat: CharacterStat = Depends(get_character_stats),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterStat:
    return await crud.character_update(session=session, character_stat=character_stat,
                                       character_stats_update=character_stats_update)


@character_stats_router.delete(
    "/delete/{character_stats_id}/",
    description="Delete the Character Stat object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_stats_delete(
        character: CharacterStat = Depends(get_character_stats),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_stat_delete(session=session, character=character)
