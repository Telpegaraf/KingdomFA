from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.schemas.domain import DomainBase, DomainUpdate
from api_v1.models.domain import Domain


async def domain_list(session: AsyncSession):
    stmt = select(Domain).order_by(Domain.id)
    result: Result = await session.execute(stmt)
    domains = result.scalars().all()
    return list(domains)


async def domain_detail(session: AsyncSession, domain_id: int) -> Domain | None:
    return await session.get(Domain, domain_id)


async def domain_create(session: AsyncSession, domain_in: DomainBase) -> Domain:
    domain = Domain(**domain_in.model_dump())
    session.add(domain)
    await session.commit()
    await session.refresh(domain)
    return domain


async def domain_update(
        domain_update: DomainUpdate,
        domain: Domain,
        session: AsyncSession,
) -> Domain:
    for name, value in domain_update.model_dump(exclude_unset=True).items():
        setattr(domain, name, value)
    await session.commit()
    return domain


async def domain_delete(domain: Domain, session: AsyncSession) -> None:
    await session.delete(domain)
    await session.commit()
