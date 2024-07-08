from fastapi import status, Depends, APIRouter
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud import user as crud
from api_v1.dependencies.get_object import get_object_by_id_dependency
from api_v1.models import user as models
from api_v1.schemas import user as schemas
from auth.utils import get_current_token_payload
from database import db_helper

http_bearer = HTTPBearer()

user_router = APIRouter(prefix="/user", tags=["Users"])


@user_router.get(
    "/{object_id}/",
    response_model=schemas.UserRead,
    description="Return information about User, depending on ID",
    dependencies=[Depends(http_bearer)]
)
async def user_detail(
        payload: dict = Depends(get_current_token_payload),
        user: models.User = Depends(get_object_by_id_dependency(models.User))
):
    return user


@user_router.get(
    "/",
    response_model=list[schemas.UserRead],
    description="Return Information about all Users",
    dependencies=[Depends(http_bearer)]
)
async def user_list(
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.user_list(session=session)
    return result


@user_router.post(
    "/create/",
    response_model=schemas.UserBase,
    description="Create a new User",
    status_code=status.HTTP_201_CREATED
)
async def user_create(
        user_in: schemas.UserBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.user_create(user_in=user_in, session=session)
    return result


@user_router.patch(
    "/change_password/{object_id}/",
    description="Change password for User, depending on ID, if old password is correct",
    dependencies=[Depends(http_bearer)]
)
async def user_change_password(
        user_in: schemas.UserUpdatePassword,
        payload: dict = Depends(get_current_token_payload),
        user: models.User = Depends(get_object_by_id_dependency(models.User)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.change_password(
        user_in=user_in,
        user=user,
        session=session
    )


@user_router.delete(
    "/user_delete/{object_id}/",
    description="Delete User, depending on ID",
    dependencies=[Depends(http_bearer)],
    status_code=status.HTTP_204_NO_CONTENT
)
async def user_delete(
        payload: dict = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        user: models.User = Depends(get_object_by_id_dependency(models.User))
):
    await crud.user_delete(user=user, session=session)
