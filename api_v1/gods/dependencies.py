from fastapi import Path, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from api_v1.gods import models, crud
from database import db_helper


async def get_domain_by_id(
        domain_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> models.Domain:
    domain = await crud.domain_detail(domain_id=domain_id, session=session)
    if domain is not None:
        return domain
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Domain {domain_id} isn't found",
    )
