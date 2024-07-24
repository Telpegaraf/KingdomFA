from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from api_v1.schemas.equipment import weapon as schemas
from api_v1.models.equipment import Weapon
from api_v1.crud.equipment import weapon as crud
from api_v1.dependencies.equipment.weapon import get_weapon

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
    "/create/",
    description="Create a new Weapon object",
    #response_model=schemas.Weapon
)
async def weapon_create(
        weapon_in: schemas.WeaponCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.weapon_create(session=session, weapon_in=weapon_in)


@weapon_router.patch(
    "/update/",
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
    "/delete/",
    description="Delete the Weapon object, depending on ID",
)
async def weapon_delete(
        weapon: Weapon = Depends(db_helper.scoped_session_dependency),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.weapon_delete(session=session, weapon=weapon)
