from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from fastapi.security import OAuth2PasswordBearer

from api_v1.models.user import User

import database
from auth import utils
from auth.helpers import (
    REFRESH_TOKEN_TYPE
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/jwt/login/",
)


async def decode_refresh_token(
        refresh_token: str,
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency),
):
    payload = utils.decode_jwt(refresh_token)
    username = payload.get("sub")
    type_token = payload.get("type")
    if type_token != REFRESH_TOKEN_TYPE:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token type: {type_token!r}, expected {REFRESH_TOKEN_TYPE!r}",
        )

    stmt = select(User).where(User.username == username)
    result = await session.execute(stmt)
    user = result.scalars().first()

    return user
