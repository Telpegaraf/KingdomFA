from fastapi import APIRouter, Depends, Path
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from api_v1.models import equipment as models
from api_v1.dependencies import get_object_by_id, get_object_by_id_dependency
from api_v1.models.enum import equipment_model_mapping, EquipmentEnum

http_bearer = HTTPBearer()


equipment_router = APIRouter(prefix="/equipment", tags=["Equipment"])


@equipment_router.get(
    "/{model_name}/{object_id}/",
    description="Return the equipment object, depending on ID",
)
async def object_detail(
        model_name: EquipmentEnum = Path(...),
        object_id: int = Path(...),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await get_object_by_id(
        model=equipment_model_mapping[model_name],
        object_id=object_id,
        session=session
    )
