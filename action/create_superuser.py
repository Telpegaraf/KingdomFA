import asyncio
import contextlib

from database import db_helper
from api_v1.schemas.user_test import UserCreate
from api_v1.dependencies.authentication.user_manager import get_user_manager
from api_v1.dependencies.authentication.users import get_users_db
from api_v1.authentication.user_manager import UserManager
from api_v1.models.fastapi_users import TestUser
from core.config import settings


get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


default_email = settings.super_user.get("super_user_email")
default_password = settings.super_user.get("super_user_password")
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
        user_manager: UserManager,
        user_create: UserCreate
) -> TestUser:
    user = await user_manager.create(
        user_create=user_create,
        safe=False
    )
    return user


async def create_superuser(
        email: str = default_email,
        password: str = default_password,
        is_active: bool = default_is_active,
        is_superuser: bool = default_is_superuser,
        is_verified: bool = default_is_verified
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified
    )
    async with db_helper.session_factory() as session:
        async with get_users_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create
                )

if __name__ == "__main__":
    asyncio.run(create_superuser())
