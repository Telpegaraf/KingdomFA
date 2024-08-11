from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from kingdom.models import equipment as models
from kingdom.crud.equipment import item as crud
from kingdom.schemas.equipment import item as schemas
from kingdom.dependencies.equipment.item import get_item


http_bearer = HTTPBearer()

item_router = APIRouter(prefix="/armor", tags=["Armor"])


@item_router.get(
    "/{item_id}/",
    description="Return the Item object, depending on ID",
    response_model=schemas.ItemRead
)
async def ger_item_detail(
        item: models.Armor = Depends(get_item),
):
    return item


@item_router.get(
    "/",
    description="Return all Item object",
    response_model=list[schemas.Item]
)
async def get_item_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.item_list(session=session)


@item_router.post(
    "/",
    description="Create a new Item object",
    response_model=schemas.Item
)
async def item_create(
        item_in: schemas.ItemCreateUpdate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.item_create(session=session, item_in=item_in)


@item_router.patch(
    "/{item_id}/",
    description="Update Item object, depending on ID",
    response_model=schemas.ItemRead
)
async def item_update(
        item_update: schemas.ItemCreateUpdate,
        item: models.Item = Depends(get_item),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.item_update(
        item_update=item_update,
        item=item,
        session=session
    )


@item_router.delete(
    "/{item_id}/",
    description="Delete Item object, depending on ID"
)
async def item_delete(
        item: models.Item = Depends(get_item),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.item_delete(session=session, item=item)
