from asyncpg import UniqueViolationError
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.models.domain import Domain
from api_v1.models.god import God
from api_v1.schemas.god import GodBase
from api_v1.models.associations.god_domain_association import GodDomainAssociation


async def god_create(god_in: GodBase, session: AsyncSession) -> God:
    god = God(**god_in.model_dump())
    session.add(god)
    await session.commit()
    await session.refresh(god)
    return god


async def god_detail(god_id: int, session: AsyncSession) -> God | None:
    return await session.scalar(
        select(God)
        .where(God.id == god_id)
        .options(
            selectinload(God.domains)
        )
    )
