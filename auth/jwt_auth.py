from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from api_v1.schemas.user import UserValidate
from api_v1.models.user import User

import database
from auth import utils
from auth.helpers import (
    TOKEN_TYPE_FIELD,
    ACCESS_TOKEN_TYPE,
    REFRESH_TOKEN_TYPE
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/jwt/login/",
)


async def decode_refresh_token(
        refresh_token: str,
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
):
    payload = utils.decode_jwt(refresh_token)
    username = payload.get("sub")

    stmt = select(User).where(User.username == username)
    result = await session.execute(stmt)
    user = result.scalars().first()

    return user
