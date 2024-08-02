
from datetime import timedelta

from auth import utils as auth_utils
from core.config import settings
from api_v1.schemas import user as schemas


TOKEN_TYPE_FIELD = "type"
ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"


def create_jwt(
    token_type: str,
    token_data: dict,
    expire_minutes: int = settings.jwt_settings.get('access_token_expire_minutes'),
    expire_timedelta: timedelta | None = None,
) -> str:
    jwt_payload = {TOKEN_TYPE_FIELD: token_type}
    jwt_payload.update(token_data)
    return auth_utils.encode_jwt(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta,
    )


def create_access_token(user: schemas.UserValidate) -> str:
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
        "id": user.id,
        "is_superuser": user.is_superuser
    }
    return create_jwt(
        token_type=ACCESS_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_minutes=settings.jwt_settings.get('access_token_expire_minutes'),
    )


def create_refresh_token(user: schemas.UserValidate) -> str:
    jwt_payload = {
        "sub": user.username,
    }
    return create_jwt(
        token_type=REFRESH_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_timedelta=timedelta(days=settings.jwt_settings.get('refresh_token_expire_days')),
    )
