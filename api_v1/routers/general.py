from fastapi import APIRouter, status, Depends, Path
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi.responses import ORJSONResponse

from api_v1.dependencies.dependencies import get_object_by_id
from api_v1.schemas import general as schemas
from api_v1.crud import general as crud
from auth.utils import get_current_token_payload
from database import db_helper
from api_v1.models.enum import (
    ModelName,
    ModelDescription,
    ModelNameDescription,
    model_mapping,
    model_description_mapping,
    model_name_description_mapping
)


http_bearer = HTTPBearer()

general_router = APIRouter(prefix="/general", tags=["General"], dependencies=[Depends(http_bearer)])


@general_router.get(
    "/{model_name}}{object_id}/",
    description="Returns information about an object, depending on the specified model and object."
                " Returns ID, name and description if this field is present in the model",
)
async def object_detail(
        payload: dict = Depends(get_current_token_payload),
        model_name: ModelNameDescription = Path(...),
        object_id: int = Path(...),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await get_object_by_id(
        model=model_name_description_mapping[model_name],
        object_id=object_id,
        session=session
    )


@general_router.get(
    "/{model_name}/",
    description="Returns information about all objects, depending on the specified model and object."
                " Returns ID, name and description if this field is present in the model"
)
async def object_list(
        payload: dict = Depends(get_current_token_payload),
        model_name: ModelNameDescription = Path(...),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.object_list(
        model=model_name_description_mapping[model_name],
        session=session
    )


@general_router.post(
    "/{model_name}/create/",
    description="Create new object, depending on the specified model"
)
async def object_create(
        object_in: schemas.GeneralBase,
        payload: dict = Depends(get_current_token_payload),
        model_name: ModelName = Path(...),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.object_create(
        model=model_mapping[model_name],
        object_in=object_in,
        session=session
    )


@general_router.post(
    "/{model_name}/create_with_description/",
    description="Create new object, depending on the specified model"
)
async def object__with_description_create(
        object_in: schemas.GeneralDescriptionBase,
        payload: dict = Depends(get_current_token_payload),
        model_name: ModelDescription = Path(...),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.object_create(
        model=model_mapping[model_name],
        object_in=object_in,
        session=session
    )


@general_router.patch(
    "/{model_name}/{object_id}/update/",
    description="Update an object, depending on the specified model and ID"
)
async def object_update(
        object_update: schemas.GeneralBase,
        payload: dict = Depends(get_current_token_payload),
        model_name: ModelName = Path(...),
        object_id: int = Path(),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    object = await get_object_by_id(
        model=model_mapping[model_name],
        object_id=object_id,
        session=session
    )
    return await crud.object_update(
        session=session,
        object=object,
        object_update=object_update
    )


@general_router.patch(
    "/{model_name}/{object_id}/update_with_description/",
    description="Partial or full update an object, depending on the specified model and ID"
)
async def object_update(
        object_update: schemas.GeneralDescriptionBase,
        payload: dict = Depends(get_current_token_payload),
        model_name: ModelDescription = Path(...),
        object_id: int = Path(),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    object = await get_object_by_id(
        model=model_description_mapping[model_name],
        object_id=object_id,
        session=session
    )
    return await crud.object_update_with_description(
        session=session,
        object=object,
        object_update=object_update
    )


@general_router.delete(
    "/{model_name}/{object_id}/delete/",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete an object, depending on the specified model and ID"
)
async def object_delete(
        model_name: ModelNameDescription = Path(...),
        payload: dict = Depends(get_current_token_payload),
        object_id: int = Path(),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    object = await get_object_by_id(
        model=model_name_description_mapping[model_name],
        object_id=object_id,
        session=session
    )
    await crud.object_delete(
        object=object,
        session=session
    )
