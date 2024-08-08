from typing import TYPE_CHECKING
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable, SQLAlchemyAccessTokenDatabase
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from kingdom.types.user_id import UserIdType
from kingdom.models.base_model import Base, MainBase
from kingdom.models.mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class TestUser(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)


class AccessToken(MainBase, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        (ForeignKey("test_users.id", ondelete="CASCADE")),
        nullable=False
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
