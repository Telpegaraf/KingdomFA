from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from kingdom.schemas import character_class as schemas
from kingdom.models import character_class as models
from kingdom.crud import character_class as crud
from kingdom.dependencies.get_object import get_object_by_id_dependency
from auth.utils import get_current_token_payload
from database import db_helper

http_bearer = HTTPBearer()

character_class_router = APIRouter(
    prefix="/character_class",
    tags=["Character Class"],
    dependencies=[Depends(http_bearer)]
)


@character_class_router.get(
    "/{object_id}/",
    description="Return information about character class, depending on ID",
    response_model=schemas.CharacterClassBase
)
async def character_class_detail(
        payload: dict = Depends(get_current_token_payload),
        character_class: models.CharacterClass = Depends(get_object_by_id_dependency(models.CharacterClass)),
):
    return character_class


@character_class_router.get(
    "/",
    description="Return information about all character classes",
    response_model=list[schemas.CharacterClass]
)
async def character_class_list(
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.character_class_list(
        session=session
    )
    return result


@character_class_router.post(
    "/",
    description="Create a new character class.",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.CharacterClassBase
)
async def character_class_create(
        character__class_in: schemas.CharacterClassBase,
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.character_class_create(
        character_class_in=character__class_in,
        session=session
    )


@character_class_router.patch(
    "/{object_id}/",
    description=f"Update information about character class, depending on ID.",
    response_model=schemas.CharacterClass
)
async def character_class_update(
        character_update: schemas.CharacterClassBase,
        payload: dict = Depends(get_current_token_payload),
        character_class: models.CharacterClass = Depends(get_object_by_id_dependency(models.CharacterClass)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.character_class_update(
        character_class_update=character_update,
        character_class=character_class,
        session=session
    )


@character_class_router.delete(
    "/{object_id}/",
    description="Delete a character class, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def character_class_delete(
        payload: dict = Depends(get_current_token_payload),
        character_class: models.CharacterClass = Depends(get_object_by_id_dependency(models.CharacterClass)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.character_class_delete(
        character_class=character_class,
        session=session
    )
