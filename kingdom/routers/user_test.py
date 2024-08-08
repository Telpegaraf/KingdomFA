from fastapi import APIRouter
from kingdom.routers.fa_users import fastapi_users
from kingdom.dependencies.authentication.backend import authentication_backend
from kingdom.schemas.user_test import UserRead, UserCreate

auth_router = APIRouter(prefix="/auth/jwt", tags=["AuthJWT"])


#/login /logout
auth_router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)

#/register

auth_router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate)
)