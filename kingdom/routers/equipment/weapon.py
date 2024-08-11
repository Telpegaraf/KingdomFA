from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from kingdom.schemas.equipment import weapon as schemas
from kingdom.models.equipment import Weapon
from kingdom.crud.equipment import weapon as crud
from kingdom.dependencies.equipment.weapon import get_weapon

http_bearer = HTTPBearer()

weapon_router = APIRouter(prefix="/weapon", tags=["Weapon"])


@weapon_router.get(
    "/{weapon_id}/",
    description="Return the Weapon object, depending on ID",
    response_model=schemas.WeaponRead
)
async def weapon_detail(
        weapon: Weapon = Depends(get_weapon)
):
    return weapon


@weapon_router.get(
    "/",
    description="Return all Weapons objects",
    response_model=list[schemas.Weapon]
)
async def weapon_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.weapon_list(session=session)


@weapon_router.post(
    "/",
    description="Create a new Weapon object",
    response_model=schemas.Weapon,
    status_code=status.HTTP_201_CREATED
)
async def weapon_create(
        weapon_in: schemas.WeaponCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.weapon_create(session=session, weapon_in=weapon_in)


@weapon_router.patch(
    "/{weapon_id}/",
    description="Update the Weapon object, depending on ID",
    response_model=schemas.WeaponBase
)
async def weapon_update(
        weapon_update: schemas.WeaponUpdate,
        weapon: Weapon = Depends(get_weapon),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.weapon_update(weapon_update=weapon_update, weapon=weapon, session=session)


@weapon_router.delete(
    "/{weapon_id}/",
    description="Delete the Weapon object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def weapon_delete(
        weapon: Weapon = Depends(get_weapon),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.weapon_delete(session=session, weapon=weapon)
