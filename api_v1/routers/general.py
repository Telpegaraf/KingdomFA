from fastapi import APIRouter, status, Depends, Path, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.dependencies import get_object_by_id_dependency, get_object_by_id
from api_v1.schemas import general as schemas
from api_v1.models import general as models
from api_v1.crud import general as crud
from auth.utils import get_current_token_payload
from database import db_helper

from enum import Enum

http_bearer = HTTPBearer()

general_router = APIRouter(prefix="/general", tags=["General"])
#general_router = APIRouter(prefix="/general", tags=["General"], dependencies=[Depends(http_bearer)])


class ModelName(str, Enum):
    damage_type = 'damage_type'
    action = 'action'
    prerequisite = 'prerequisite'
    requirements = 'requirements'
    trigger = 'trigger'
    skills = 'skills'
    weapon_mastery = 'weapon_mastery'
    feat_trait = 'feat_trait'


model_mapping = {
    "damage_type": models.DamageType,
    "action": models.Action,
    'prerequisite': models.Prerequisite,
    'requirements': models.Requirements,
    'trigger': models.Trigger,
    'skills': models.Skills,
    'weapon_mastery': models.WeaponMastery,
    'feat_trait': models.FeatTrait
    }


@general_router.get("/{model_name}}{object_id}/")
async def object_detail(
        model_name: ModelName = Path(...),
        object_id: int = Path(...),
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
):
    return await get_object_by_id(model=model_mapping[model_name], object_id=object_id, session=session)


@general_router.get("/{model_name}/")
async def object_list(
        model_name: ModelName = Path(...),
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
):
    return await crud.object_list(
        model=model_mapping[model_name],
        session=session
    )
