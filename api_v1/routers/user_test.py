from fastapi import APIRouter
from api_v1.routers.fa_users import fastapi_users
from api_v1.dependencies.authentication.backend import authentication_backend
from api_v1.schemas.user_test import UserRead, UserCreate

auth_router = APIRouter(prefix="/auth/jwt", tags=["AuthJWT"])


#/login /logout
auth_router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)

#/register

auth_router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate)
)