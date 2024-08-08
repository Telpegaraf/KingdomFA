from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api_v1.schemas.religion import (
    DomainBase,
    DomainUpdate,
    GodCreateUpdate
)
from core.models.religion import Domain, God
from api_v1.utils.model_result import get_model_m2m_result


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


async def god_create(god_in: GodCreateUpdate, session: AsyncSession) -> God:
    domains = await get_model_m2m_result(model=Domain, object_list=god_in.domains, session=session)

    god_data = god_in.dict(exclude={"domains"})

    god = God(
        **god_data,
        domains=domains
    )

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


async def god_list(session: AsyncSession):
    stmt = select(God).options(selectinload(God.domains)).order_by(God.id)
    result: Result = await session.execute(stmt)
    gods = result.scalars().all()
    return gods


async def god_update(
        god_update: GodCreateUpdate,
        god: God,
        session: AsyncSession
) -> God:
    for key, value in god_update.model_dump(exclude_unset=True).items():
        if hasattr(god, key) and key != "domains":
            setattr(god, key, value)
    domains = await get_model_m2m_result(model=Domain, object_list=god_update.domains, session=session)
    god.domains.clear()
    for value in domains:
        god.domains.append(value)
    await session.commit()
    await session.refresh(god)
    return god


async def god_delete(
        god: God,
        session: AsyncSession
) -> None:

    await session.delete(god)
    await session.commit()
