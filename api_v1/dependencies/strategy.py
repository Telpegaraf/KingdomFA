from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from typing import TYPE_CHECKING, Annotated

from api_v1.dependencies.access_token import get_access_tokens_db
from core.config import settings
if TYPE_CHECKING:
    from api_v1.models.access_token import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
        access_tokens_db: Annotated[
            "AccessTokenDatabase[AccessToken]",
            Depends(get_access_tokens_db)]

) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_tokens_db,
        lifetime_seconds=settings.jwt_settings.get("access_token_expire_minutes"))