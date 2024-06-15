from fastapi import status, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud import user as crud
from api_v1.models import user as models
from api_v1.schemas import user as schemas
from api_v1.dependencies import get_object_by_id_dependency
from database import db_helper

user_router = APIRouter(prefix="/user", tags=["Users"])


@user_router.get("/{object_id}/", response_model=schemas.UserRead)
async def user_detail(
        user: models.User = Depends(get_object_by_id_dependency(models.User))
):
    return user


@user_router.get("/", response_model=list[schemas.UserRead])
async def user_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.user_list(session=session)
    return result


@user_router.post("/create/", response_model=schemas.UserBase, status_code=status.HTTP_201_CREATED)
async def user_create(
        user_in: schemas.UserBase,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.user_create(user_in=user_in, session=session)
    return result


@user_router.patch("/change_password/{object_id}")
async def user_change_password(
        user_in: schemas.UserUpdatePassword,
        user: models.User = Depends(get_object_by_id_dependency(models.User)),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.change_password(
        user_in=user_in,
        user=user,
        session=session
    )
