from fastapi import status, Depends, APIRouter
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud import god as crud
from api_v1.schemas import god as schemas
from api_v1.models import god as models
from api_v1.dependencies.dependencies import get_object_by_id_dependency
from auth.utils import get_current_token_payload
from database import db_helper

http_bearer = HTTPBearer(auto_error=False)

god_router = APIRouter(prefix="/god", tags=["Gods"], dependencies=[Depends(http_bearer)])


@god_router.get("/{object_id}/")
async def god_detail(
        payload: dict = Depends(get_current_token_payload),
        god: models.God = Depends(get_object_by_id_dependency(models.God))
):
    return god


@god_router.get("/", response_model=list[schemas.God])
async def god_list(
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.god_list(session=session)
    return result


@god_router.post("/create/", status_code=status.HTTP_201_CREATED)
async def god_create(
        god_in: schemas.GodBase,
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.god_create(god_in=god_in, session=session)
    return result


@god_router.patch("/update/{object_id}/")
async def update(
        god_update: schemas.GodBase,
        payload: dict = Depends(get_current_token_payload),
        god: models.God = Depends(get_object_by_id_dependency(models.God)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.god_update(
        god_update=god_update,
        god=god,
        session=session
    )


@god_router.delete("/delete/{object_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        payload: dict = Depends(get_current_token_payload),
        god: models.God = Depends(get_object_by_id_dependency(models.God)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.god_delete(god=god, session=session)
