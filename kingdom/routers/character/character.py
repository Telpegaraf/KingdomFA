from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from kingdom.models.character import Character
from kingdom.schemas.character import character as schemas
from kingdom.crud.character import character as crud
from kingdom.dependencies.character.character import get_character
from auth.utils import get_current_token_payload
from database import db_helper


http_bearer = HTTPBearer()

character_router = APIRouter(prefix="/character", tags=["Character"], dependencies=[Depends(http_bearer)])


@character_router.get(
    "/{character_id}/",
    description="Return the character object, depending on ID",
    response_model=schemas.CharacterRead
)
async def character_detail(character: Character = Depends(get_character)) -> Character:
    return character


@character_router.get(
    "/",
    description="Return all character objects",
    response_model=list[schemas.Character]
)
async def character_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[Character]:
    return await crud.character_list(session=session)


@character_router.post(
    "/",
    description="Create a new character object",
    response_model=schemas.CharacterRead,
    status_code=status.HTTP_201_CREATED
)
async def character_create(
        character_in: schemas.CharacterCreate,
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Character:
    return await crud.character_create(session=session, character_in=character_in)


@character_router.patch(
    "/{character_id}/",
    description="Update the character object, depending on ID",
    response_model=schemas.CharacterRead
)
async def character_update(
        character_update: schemas.CharacterUpdate,
        character: Character = Depends(get_character),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Character:
    return await crud.character_update(session=session, character=character, character_update=character_update)


@character_router.delete(
    "/{character_id}/",
    description="Delete the character object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_delete(
        character: Character = Depends(get_character),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_delete(session=session, character=character)
