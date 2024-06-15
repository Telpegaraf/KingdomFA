import bcrypt
from fastapi import Depends, HTTPException, status
from jwt import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
import jwt
from core.config import settings
from database import db_helper
from api_v1.schemas.user import UserValidate
from api_v1.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/jwt/login/",
)


TOKEN_TYPE_FIELD = "type"
ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"


def encode_jwt(
    payload: dict,
    private_key: str = settings.jwt_settings.get("private_key_path").read_text(),
    algorithm: str = settings.jwt_settings.get("algorithm"),
    expire_minutes: int = settings.jwt_settings.get("access_token_expire_minutes"),
    expire_timedelta: timedelta | None = None,
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = expire_timedelta + now
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.jwt_settings.get("public_key_path").read_text(),
    algorithms: str = settings.jwt_settings.get("algorithm")
):
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithms]
    )
    return decoded


def hash_password(password):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    string_password = hashed_password.decode('utf8')
    return string_password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
) -> dict:
    try:
        payload = decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
        )
    token_type = payload.get('type')
    if token_type != ACCESS_TOKEN_TYPE:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token type: {token_type!r}, expected {ACCESS_TOKEN_TYPE!r}",
        )
    return payload


def validate_token_type(
    payload: dict,
    token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"invalid token type {current_token_type!r} expected {token_type!r}",
    )


async def get_user_by_token_sub(
        payload: dict,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> UserValidate:
    print(11111)
    username: str | None = payload.get("sub")
    print(username)
    stmt = select(User).where(User.username == username)
    result = await session.execute(stmt)
    #if user := users_db.get(username):
    if user := result.scalars().first():
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_auth_user_from_token_of_type(
        token_type: str,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    async def get_auth_user_from_token(
        payload: dict = Depends(get_current_token_payload),
    ) -> UserValidate:
        validate_token_type(payload, token_type)
        return await get_user_by_token_sub(payload, session=session)

    return get_auth_user_from_token


class UserGetterFromToken:
    def __init__(self, token_type: str):
        self.token_type = token_type

    async def __call__(
        self,
        payload: dict = Depends(get_current_token_payload),
    ):
        validate_token_type(payload, self.token_type)
        return await get_user_by_token_sub(payload)


get_current_auth_user = get_auth_user_from_token_of_type(ACCESS_TOKEN_TYPE)

get_current_auth_user_for_refresh = UserGetterFromToken(REFRESH_TOKEN_TYPE)
