from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from kingdom.models.character import CharacterWeaponMastery
from kingdom.schemas.character import character_weapon_mastery as schemas
from kingdom.crud.character import character_weapon_mastery as crud
from kingdom.dependencies.character.character_weapon_mastery import get_character_weapon_mastery
from database import db_helper


http_bearer = HTTPBearer()

character_weapon_mastery_router = APIRouter(prefix="/character_weapon_mastery", tags=["Character Weapon"])


@character_weapon_mastery_router.get(
    "/{character_weapon_mastery_id}/",
    description="Return the Character Skill Mastery object, depending on ID",
    response_model=schemas.CharacterWeaponMasteryRead
)
async def character_weapon_mastery_detail(
        character: CharacterWeaponMastery = Depends(get_character_weapon_mastery)
) -> CharacterWeaponMastery:
    return character


@character_weapon_mastery_router.get(
    "/",
    description="Return all Character Weapon Mastery objects",
    response_model=list[schemas.CharacterWeaponMastery]
)
async def character_weapon_mastery_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterWeaponMastery]:
    return await crud.character_weapon_mastery_list(session=session)


@character_weapon_mastery_router.post(
    "/",
    description="Create a new Character Weapon Mastery object",
    response_model=schemas.CharacterWeaponMastery,
    status_code=status.HTTP_201_CREATED
)
async def character_weapon_mastery_create(
        character_weapon_mastery_in: schemas.CharacterWeaponMasteryCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterWeaponMastery:
    return await crud.character_weapon_mastery_create(
        session=session,
        character_weapon_mastery_in=character_weapon_mastery_in
    )


@character_weapon_mastery_router.patch(
    "/{character_weapon_mastery_id}/",
    description="Update the Character Weapon Mastery object, depending on ID",
    response_model=schemas.CharacterWeaponMasteryRead
)
async def character_weapon_mastery_update(
        character_weapon_mastery_update: schemas.CharacterWeaponMasteryUpdate,
        character_weapon_mastery: CharacterWeaponMastery = Depends(get_character_weapon_mastery),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterWeaponMastery:
    return await crud.character_weapon_mastery_update(
        session=session,
        character_weapon_mastery=character_weapon_mastery,
        character_weapon_mastery_update=character_weapon_mastery_update
    )


@character_weapon_mastery_router.delete(
    "/{character_weapon_mastery_id}/",
    description="Delete the Character Weapon Mastery object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_weapon_mastery_delete(
        character: CharacterWeaponMastery = Depends(get_character_weapon_mastery),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_weapon_mastery_delete(session=session, character=character)
