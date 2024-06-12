from fastapi import status, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud import god as crud
from api_v1.schemas import god as schemas
from api_v1.models import god as models
from api_v1.dependencies.god import get_god_by_id
from database import db_helper


god_router = APIRouter(prefix="/god")


@god_router.post("/create/", status_code=status.HTTP_201_CREATED)
async def god_create(
        god_in: schemas.GodBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    result = await crud.god_create(god_in=god_in, session=session)
    return result


@god_router.get("/{god_id}/")
async def god_detail(
        god: models.God = Depends(dependency=get_god_by_id)
):
    return god
