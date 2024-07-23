from fastapi import APIRouter, Depends, Path
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from api_v1.models import equipment as models
from api_v1.crud.equipment import armor as crud
from api_v1.schemas.equipment import armor as schemas
from api_v1.dependencies.get_object import get_object_by_id_dependency


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


@armor_router.get(
    "/{armor_id}/",
    description="Return the armor object, depending on ID",
    response_model=schemas.ArmorRead
)
async def ger_armor_detail(
        armor_id: int = Path(),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.armor_detail(session=session, armor_id=armor_id)


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


# @armor_router.patch(
#     "/update/{object_id}/",
#     description="Update armor object, depending on ID"
# )
# async def armor_update(
#         armor_update: schemas.WornUpdate,
#         armor: models.Armor = Depends(get_object_by_id_dependency(models.Armor)),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await crud.armor_update(
#         armor_update=armor_update,
#         armor=armor,
#         session=session
#     )
#
#
# @worn_router.delete(
#     "/{object_id}/delete/",
#     description="Delete worn object, depending on ID"
# )
# async def worn_delete(
#         worn: models.Worn = Depends(get_object_by_id_dependency(models.Worn)),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await crud.worn_delete(
#         session=session,
#         worn=worn
#     )
