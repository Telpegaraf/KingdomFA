from fastapi import Depends
from typing import TYPE_CHECKING, Annotated
from database import db_helper

from core.models.fastapi_users import TestUser

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
        session: Annotated[
            "AsyncSession",
            Depends(db_helper.scoped_session_dependency)
        ]
):
    yield TestUser.get_db(session=session)
