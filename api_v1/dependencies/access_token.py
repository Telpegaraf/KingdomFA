from fastapi import Depends
from typing import TYPE_CHECKING, Annotated
from database import db_helper

from api_v1.models.access_token import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
        session: Annotated[
            "AsyncSession",
            Depends(db_helper.scoped_session_dependency)
        ]
):
    yield AccessToken.get_db(session=session)
