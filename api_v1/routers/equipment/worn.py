from fastapi import APIRouter, Depends, Path
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from api_v1.models import equipment as models
from api_v1.crud.equipment import worn as crud
from api_v1.dependencies.dependencies import get_object_by_id, get_object_by_id_dependency
from api_v1.models.enum import equipment_model_mapping, EquipmentEnum
from api_v1.schemas.equipment import worn as schemas

http_bearer = HTTPBearer()


worn_router = APIRouter(prefix="/worn_items", tags=["Worn Items"])


@worn_router.get(
    "/{object_id}/",
    description="Return the worn object, depending on ID",
)
async def get_worn_item(
        worn: models.Worn = Depends(get_object_by_id_dependency(models.Worn))
):
    return worn


@worn_router.get(
    "/",
    description="Return all worn object",
)
async def get_worn_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_item_list(session=session)


@worn_router.post(
    "/create/",
    description="Create a new worn object",
    #response_model=schemas.Worn
)
async def worn_create(
        worn_in: schemas.WornCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_create(session=session, worn_in=worn_in)


@worn_router.patch(
    "/update/{object_id}/",
    description="Update worn object, depending on ID"
)
async def worn_update(
        worn_update: schemas.WornUpdate,
        worn: models.Worn = Depends(get_object_by_id_dependency(models.Worn)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_update(
        worn_update=worn_update,
        worn=worn,
        session=session
    )


@worn_router.delete(
    "/{object_id}/delete/",
    description="Delete worn object, depending on ID"
)
async def worn_delete(
        worn: models.Worn = Depends(get_object_by_id_dependency(models.Worn)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_delete(
        session=session,
        worn=worn
    )
