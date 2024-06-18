from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.schemas import character_class as schema
from api_v1.models import character_class as models
from api_v1.crud import character_class as crud
from api_v1.dependencies import get_object_by_id_dependency
from database import db_helper

http_bearer = HTTPBearer()

character_class_router = APIRouter(prefix="/character_class", tags=["Character Clss"])


@character_class_router.get("/{object_id}/")
async def character_class_detail(
        character_class: models.CharacterClass = Depends(get_object_by_id_dependency(models.CharacterClass)),
):
    return character_class


@character_class_router.post("/create/", status_code=status.HTTP_201_CREATED, response_model=schema.CharacterClassBase)
async def character_class_create(
        character__class_in: schema.CharacterClassBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.character_class_create(
        character_class_in=character__class_in,
        session=session
    )

