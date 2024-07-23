from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from api_v1.models import equipment as models
from api_v1.crud.equipment import worn as crud
from api_v1.dependencies.get_object import get_object_by_id_dependency
from api_v1.dependencies.equipment.worn import get_worn
from api_v1.schemas.equipment import worn as schemas

http_bearer = HTTPBearer()


worn_router = APIRouter(prefix="/worn_items", tags=["Worn Items"])


@worn_router.get(
    "/{worn_id}/",
    description="Return the worn object, depending on ID",
    response_model=schemas.WornRead
)
async def get_worn_item(
        worn: models.Worn = Depends(get_worn)
):
    return worn


@worn_router.get(
    "/",
    description="Return all worn object",
    response_model=list[schemas.Worn]
)
async def get_worn_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_item_list(session=session)


@worn_router.post(
    "/create/",
    description="Create a new worn object",
    response_model=schemas.Worn
)
async def worn_create(
        worn_in: schemas.WornCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_create(session=session, worn_in=worn_in)


@worn_router.patch(
    "/update/{worn_id}/",
    description="Update worn object, depending on ID",
    response_model=schemas.WornRead
)
async def worn_update(
        worn_update: schemas.WornUpdate,
        worn: models.Worn = Depends(get_worn),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_update(
        worn_update=worn_update,
        worn=worn,
        session=session
    )


@worn_router.delete(
    "/{worn_id}/delete/",
    description="Delete worn object, depending on ID"
)
async def worn_delete(
        worn: models.Worn = Depends(get_worn),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_delete(
        session=session,
        worn=worn
    )
