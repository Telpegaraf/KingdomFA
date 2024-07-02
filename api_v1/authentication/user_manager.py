import logging
from typing import Optional, TYPE_CHECKING
from fastapi_users import BaseUserManager, IntegerIDMixin

from core.config import settings
from api_v1.models.user_test import TestUser
from api_v1.models.base_model import Base
from api_v1.types.user_id import UserIdType
if TYPE_CHECKING:
    from fastapi import Request

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[TestUser, UserIdType]):
    reset_password_token_secret = settings.jwt_database_settings.get("reset_password_secret")
    verification_token_secret = settings.jwt_database_settings.get("verification_password_secret")

    async def on_after_register(
        self,
        user: TestUser,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has registered.",
            user.id,
        )

    async def on_after_request_verify(
        self,
        user: TestUser,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )

    async def on_after_forgot_password(
        self,
        user: TestUser,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token,
        )
