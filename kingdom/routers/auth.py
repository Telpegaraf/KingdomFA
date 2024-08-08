from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from kingdom.schemas import user as schema
from kingdom.crud.user import validate_user
from auth.helpers import create_access_token, create_refresh_token
from auth.jwt_auth import decode_refresh_token
import database

http_bearer = HTTPBearer(auto_error=False)


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"


auth_router = APIRouter(
    prefix="/auth",
    tags=["JWT"],
    dependencies=[Depends(http_bearer)]
)


@auth_router.post("/login/", response_model=TokenInfo)
async def auth_user_issue_jwt(
    user: schema.UserValidate = Depends(validate_user),
):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@auth_router.post(
    "/refresh/",
    response_model=TokenInfo,
    response_model_exclude_none=True,
)
async def auth_refresh_jwt(
    refresh_token: str,
    session: AsyncSession = Depends(database.db_helper.scoped_session_dependency),
):
    user = await decode_refresh_token(refresh_token, session)
    if user:
        access_token = create_access_token(user)
        return TokenInfo(access_token=access_token)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid refresh token",
    )
