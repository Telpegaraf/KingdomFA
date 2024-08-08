from fastapi import APIRouter, Depends, Path, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from core.models import equipment as models
from api_v1.crud.equipment import armor as crud
from api_v1.schemas.equipment import armor as schemas
from api_v1.dependencies.get_object import get_object_by_id_dependency
from api_v1.dependencies.equipment.armor import get_armor


http_bearer = HTTPBearer()

armor_router = APIRouter(prefix="/armor", tags=["Armor"])


@armor_router.get(
    "/armor_group/{object_id}",
    description="Return the armor group object, depending on id",
    response_model=schemas.ArmorGroupBase
)
async def get_armor_group_detail(
        armor_group: models.ArmorGroup = Depends(get_object_by_id_dependency(models.ArmorGroup)),
):
    return armor_group


@armor_router.get(
    "/armor_group/",
    description="Return all Armor Group objects",
    response_model=list[schemas.ArmorGroup]
)
async def get_armor_group_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.armor_group_list(session=session)


@armor_router.post(
    "/armor_group/create/",
    description="Create new Armor Group object",
    response_model=schemas.ArmorGroup,
    status_code=status.HTTP_201_CREATED
)
async def armor_group_create(
        armor_group_in: schemas.ArmorGroupBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.armor_group_create(session=session, armor_group_in=armor_group_in)


@armor_router.patch(
    "/armor_group/update/{object_id}/",
    description="Change Armor Group object",
    response_model=schemas.ArmorGroupBase
)
async def armor_group_update(
        armor_group_update: schemas.ArmorGroupBase,
        armor_group: models.ArmorGroup = Depends(get_object_by_id_dependency(models.ArmorGroup)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.armor_group_update(
        session=session,
        armor_group_update=armor_group_update,
        armor_group=armor_group
    )


@armor_router.delete(
    "/armor_group/delete/{object_id}",
    description="Delete Armor Group object",
    status_code=status.HTTP_204_NO_CONTENT
)
async def armor_group_delete(
        armor_group: models = Depends(get_object_by_id_dependency(models.ArmorGroup)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.armor_group_delete(armor_group=armor_group, session=session)


@armor_router.get(
    "/{armor_id}/",
    description="Return the armor object, depending on ID",
    response_model=schemas.ArmorRead
)
async def ger_armor_detail(
        armor: models.Armor = Depends(get_armor),
):
    return armor


@armor_router.get(
    "/",
    description="Return all armor object",
    response_model=list[schemas.Armor]
)
async def get_armor_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.armor_list(session=session)


@armor_router.post(
    "/create/",
    description="Create a new armor object",
    response_model=schemas.Armor
)
async def armor_create(
        armor_in: schemas.ArmorCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.armor_create(session=session, armor_in=armor_in)


@armor_router.patch(
    "/update/{armor_id}/",
    description="Update armor object, depending on ID",
    response_model=schemas.ArmorRead
)
async def armor_update(
        armor_update: schemas.ArmorUpdate,
        armor: models.Armor = Depends(get_armor),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.armor_update(
        armor_update=armor_update,
        armor=armor,
        session=session
    )


@armor_router.delete(
    "/{armor_id}/delete/",
    description="Delete Armor object, depending on ID"
)
async def armor_delete(
        armor: models.Armor = Depends(get_armor),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.armor_delete(session=session, armor=armor)
