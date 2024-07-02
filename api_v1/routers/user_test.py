from fastapi import APIRouter
from api_v1.routers.fa_users import fastapi_users
from api_v1.dependencies.authentication.backend import authentication_backend

router = APIRouter(prefix="auth/jwt", tags=["AuthJWT"])

router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)
