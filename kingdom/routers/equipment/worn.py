from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from kingdom.models import equipment as models
from kingdom.crud.equipment import worn as crud
from kingdom.dependencies.get_object import get_object_by_id_dependency
from kingdom.dependencies.equipment.worn import get_worn
from kingdom.schemas.equipment import worn as schemas

http_bearer = HTTPBearer()


worn_router = APIRouter(prefix="/worn_items", tags=["Worn Items"])


@worn_router.get(
    "/slot/{object_id}/",
    description="Return the slot object, depending on ID",
    response_model=schemas.SlotBase
)
async def slot_detail(
        slot: models.Slot = Depends(get_object_by_id_dependency(models.Slot)),
):
    return slot


@worn_router.get(
    "/slot/",
    description="Return all Slot objects",
    response_model=list[schemas.Slot]
)
async def slot_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.slot_list(session=session)


@worn_router.post(
    "/slot/",
    description="Create a new Slot object",
    response_model=schemas.Slot
)
async def slot_create(
        slot_in: schemas.SlotBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.slot_create(session=session, slot_in=slot_in)


@worn_router.patch(
    "/slot/{object_id}/",
    description="Update the Slot object, depending on ID",
    response_model=schemas.SlotBase
)
async def slot_update(
        slot_update: schemas.SlotBase,
        slot: models.Slot = Depends(get_object_by_id_dependency(models.Slot)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.slot_update(session=session, slot_update=slot_update, slot=slot)


@worn_router.delete(
    "/slot/{object_id}/",
    description="Delete the Slot objecs, depending on ID"
)
async def delete(
        slot: models.Slot = Depends(get_object_by_id_dependency(models.Slot)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.slot_delete(session=session, slot=slot)


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
    "/",
    description="Create a new worn object",
    response_model=schemas.Worn
)
async def worn_create(
        worn_in: schemas.WornCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.worn_create(session=session, worn_in=worn_in)


@worn_router.patch(
    "/{worn_id}/",
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
    "/{worn_id}/",
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
