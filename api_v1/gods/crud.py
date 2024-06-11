
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.gods import models, schemas
from api_v1.gods import models


async def domain_list(session: AsyncSession):
    # return db.query(models.Domain).all()
    stmt = select(models.Domain).order_by(models.Domain.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def domain_detail(session: AsyncSession, domain_id: int) -> models.Domain | None:
    return await session.get(models.Domain, domain_id)


async def domain_create(session: AsyncSession, domain_in: schemas.DomainBase) -> models.Domain:
    domain = models.Domain(**domain_in.model_dump())
    session.add(domain)
    await session.commit()
    await session.refresh(domain)
    return domain


async def domain_update(
        domain_update: schemas.DomainBase,
        domain: models.Domain,
        session: AsyncSession,
) -> models.Domain:
    for name, value in domain_update.model_dump(exclude_unset=True).items():
        setattr(domain, name, value)
    await session.commit()
    return domain


async def domain_delete(domain: models.Domain, session: AsyncSession) -> None:
    await session.delete(domain)
    await session.commit()
