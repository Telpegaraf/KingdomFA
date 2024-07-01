from fastapi_users_db_sqlalchemy.access_token import(
    SQLAlchemyBaseAccessTokenTable,
    SQLAlchemyAccessTokenDatabase
)
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from typing import TYPE_CHECKING
from api_v1.types.user_id import UserIdType
from api_v1.models.base_model import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    user_id:Mapped[UserIdType] = mapped_column(
        Integer,
        (ForeignKey("test_users.id", ondelete="CASCADE")),
        nullable=False
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
