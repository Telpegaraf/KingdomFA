from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.character import CharacterPoint
from api_v1.schemas.character import character_points as schemas
from api_v1.crud.character import character_points as crud
from api_v1.dependencies.character.character_point import get_character_point
from database import db_helper


http_bearer = HTTPBearer()

character_point_router = APIRouter(prefix="/character_point", tags=["Character Point"])


@character_point_router.get(
    "/{character_point_id}/",
    description="Return the Character Point object, depending on ID",
    response_model=schemas.CharacterPointRead
)
async def character_points_detail(character: CharacterPoint = Depends(get_character_point)) -> CharacterPoint:
    return character


@character_point_router.get(
    "/",
    description="Return all Character Point objects",
    response_model=list[schemas.CharacterPoint]
)
async def character_points_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterPoint]:
    return await crud.character_point_list(session=session)


@character_point_router.post(
    "/create/",
    description="Create a new Character Point object",
    response_model=schemas.CharacterPointRead,
    status_code=status.HTTP_201_CREATED
)
async def character_points_create(
        character_point_in: schemas.CharacterPointCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterPoint:
    return await crud.character_point_create(session=session, character_point_in=character_point_in)


@character_point_router.patch(
    "/update/{character_point_id}/",
    description="Update the Character Point object, depending on ID",
    response_model=schemas.CharacterPointRead
)
async def character_update(
        character_point_update: schemas.CharacterPointUpdate,
        character_point: CharacterPoint = Depends(get_character_point),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterPoint:
    return await crud.character_stats_update(session=session, character_point=character_point,
                                              character_point_update=character_point_update)


@character_point_router.delete(
    "/delete/{character_point_id}/",
    description="Delete the Character Point object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_points_delete(
        character: CharacterPoint = Depends(get_character_point),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_point_delete(session=session, character=character)
