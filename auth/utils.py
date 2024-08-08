import bcrypt
from fastapi import Depends, HTTPException, status
from jwt import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
import jwt
from core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.user import User
from database import db_helper

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


def get_is_super_user(
    token: str = Depends(oauth2_scheme)
) -> dict:
    payload = get_current_token_payload(token)
    is_superuser = payload.get("is_superuser")
    if not is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Access denied for current user",
        )
    return payload


def get_current_user(
        token: str = Depends(oauth2_scheme)
) -> int:
    payload = get_current_token_payload(token)
    current_user = payload.get("id")
    return current_user





