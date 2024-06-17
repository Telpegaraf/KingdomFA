from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api_v1.models.domain import Domain
from api_v1.models.god import God
from api_v1.schemas.god import GodBase


async def god_create(god_in: GodBase, session: AsyncSession) -> God:
    domain_names = [domain.name for domain in god_in.domains]
    existing_domains = await session.execute(
        select(Domain).where(Domain.name.in_(domain_names))
    )
    existing_domains = existing_domains.scalars().all()
    existing_domain_dict = {domain.name: domain for domain in existing_domains}
    domains = []
    for domain_in in god_in.domains:
        if domain_in.name in existing_domain_dict:
            domains.append(existing_domain_dict[domain_in.name])
        else:
            new_domain = Domain(name=domain_in.name)
            session.add(new_domain)
            await session.flush()
            domains.append(new_domain)

    god = God(
        name=god_in.name,
        alias=god_in.alias,
        edict=god_in.edict,
        anathema=god_in.anathema,
        areas_of_interest=god_in.areas_of_interest,
        temples=god_in.temples,
        worship=god_in.worship,
        sacred_animal=god_in.sacred_animal,
        sacred_color=god_in.sacred_color,
        chosen_weapon=god_in.chosen_weapon,
        taro=god_in.taro,
        alignment=god_in.alignment,
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
        god_update: GodBase,
        god: God,
        session: AsyncSession
) -> God:
    for key, value in god_update.model_dump(exclude_unset=True).items():
        if hasattr(god, key) and key != "domains":
            setattr(god, key, value)
    new_domains = god_update.domains
    god.domains.clear()

    for domain_data in new_domains:
        domain = await session.execute(
            select(Domain).where(Domain.name == domain_data.name)
        )
        existing_domain = domain.scalar_one_or_none()
        if existing_domain:
            god.domains.append(existing_domain)
        else:
            new_domain = Domain(name=domain_data.name)
            session.add(new_domain)
            await session.flush()
            god.domains.append(new_domain)

    await session.commit()
    await session.refresh(god)
    return god


async def god_delete(
        god: God,
        session: AsyncSession
) -> None:

    await session.delete(god)
    await session.commit()
