from fastapi import Depends
from typing import Annotated, TYPE_CHECKING
from kingdom.authentication.user_manager import UserManager
from kingdom.dependencies.authentication.users import get_users_db
if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(
        users_db: Annotated[
            "SQLAlchemyUserDatabase",
            Depends(get_users_db)
        ],
):
    yield UserManager(users_db)
