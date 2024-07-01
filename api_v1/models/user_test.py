from typing import TYPE_CHECKING
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from api_v1.types.user_id import UserIdType
from api_v1.models.base_model import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class TestUser(Base, SQLAlchemyBaseUserTable[UserIdType]):
    pass

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)