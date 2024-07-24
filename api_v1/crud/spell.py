from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.schemas.spell import SpellRead, SpellCreate, SpellUpdate
from api_v1.models.spell import Spell
from api_v1.models.general import SpellCast, SpellTrait, SpellSchool, SpellComponent, SpellTradition


async def spell_detail(session: AsyncSession, spell_id: int) -> Spell:
    return await session.scalar(
        select(Spell).
        where(Spell.id == spell_id).options(
            selectinload(Spell.spell_trait),
            selectinload(Spell.spell_school),
            selectinload(Spell.spell_cast),
            selectinload(Spell.spell_tradition),
            selectinload(Spell.spell_component)
        )
    )


async def spell_list(session: AsyncSession) -> list[Spell]:
    stmt = select(Spell).options(
            selectinload(Spell.spell_trait),
            selectinload(Spell.spell_school),
            selectinload(Spell.spell_cast),
            selectinload(Spell.spell_tradition),
            selectinload(Spell.spell_component)
        ).order_by(Spell.id)
    result: Result = await session.execute(stmt)
    spells = result.scalars().all()
    return list(spells)


async def spell_create(
        session: AsyncSession,
        spell_in: SpellCreate,
) -> Spell:
    spell_cast_result = await session.execute(
        select(SpellCast).where(SpellCast.id == spell_in.spell_cast_id)
    )
    spell_cast = spell_cast_result.scalar_one_or_none()
    if spell_cast is None:
        raise HTTPException(status_code=404, detail="Spell Cast is not found")
    spell_tradition_result = await session.execute(
        select(SpellTradition).where(SpellTradition.id == spell_in.spell_tradition_id)
    )
    spell_tradition = spell_tradition_result.scalar_one_or_none()
    if spell_tradition is None:
        raise HTTPException(status_code=404, detail="Spell Tradition is not found")
    spell_school_result = await session.execute(
        select(SpellSchool).where(SpellSchool.id == spell_in.spell_school_id)
    )
    spell_school = spell_school_result.scalar_one_or_none()
    if spell_school is None:
        raise HTTPException(status_code=404, detail="Spell School is not found")
    spell_component_result = await session.execute(
        select(SpellComponent).where(SpellComponent.id == spell_in.spell_component_id)
    )
    spell_component = spell_component_result.scalar_one_or_none()
    spell_trait_result = await session.execute(
        select(SpellTrait).where(SpellTrait.id == spell_in.spell_trait_id)
    )
    spell_trait = spell_trait_result.scalar_one_or_none()
    spell = Spell(
        name=spell_in.name,
        description=spell_in.description,
        level=spell_in.level,
        spell_range=spell_in.spell_range,
        duration=spell_in.duration,
        sustain=spell_in.sustain,
        ritual=spell_in.ritual,
        secondary_casters=spell_in.secondary_casters,
        cost=spell_in.cost,
        target=spell_in.target,
        source=spell_in.source,
        spell_cast=spell_cast,
        spell_tradition=spell_tradition,
        spell_component=spell_component,
        spell_school=spell_school,
        spell_trait=spell_trait
    )
    session.add(spell)
    await session.commit()
    await session.refresh(spell)
    return await spell_detail(session=session, spell_id=spell.id)


async def spell_update(
        session: AsyncSession,
        spell_update: SpellUpdate,
        spell: Spell
) -> Spell:
    spell_cast_result = await session.execute(
        select(SpellCast).where(SpellCast.id == spell_update.spell_cast_id)
    )
    spell_cast = spell_cast_result.scalar_one_or_none()
    if spell_cast is None:
        raise HTTPException(status_code=404, detail="Spell Cast is not found")
    spell_tradition_result = await session.execute(
        select(SpellTradition).where(SpellTradition.id == spell_update.spell_tradition_id)
    )
    spell_tradition = spell_tradition_result.scalar_one_or_none()
    if spell_tradition is None:
        raise HTTPException(status_code=404, detail="Spell Tradition is not found")
    spell_school_result = await session.execute(
        select(SpellSchool).where(SpellSchool.id == spell_update.spell_school_id)
    )
    spell_school = spell_school_result.scalar_one_or_none()
    if spell_school is None:
        raise HTTPException(status_code=404, detail="Spell School is not found")
    spell_component_result = await session.execute(
        select(SpellComponent).where(SpellComponent.id == spell_update.spell_component_id)
    )
    spell_component = spell_component_result.scalar_one_or_none()
    spell_trait_result = await session.execute(
        select(SpellTrait).where(SpellTrait.id == spell_update.spell_trait_id)
    )
    spell_trait = spell_trait_result.scalar_one_or_none()
    for key, value in spell_update.model_dump(exclude_unset=True).items():
        if hasattr(spell, key) and key not in [
            "spell_cast_id", "spell_tradition_id", "spell_component_id",
            "spell_school_id", "spell_trait_id",
        ]:
            setattr(spell, key, value)
    spell.spell_cast = spell_cast
    spell.spell_tradition = spell_tradition
    spell.spell_component = spell_component
    spell.spell_school = spell_school
    spell.spell_trait = spell_trait
    await session.commit()
    await session.refresh(spell)
    return spell


async def spell_delete(
        session: AsyncSession,
        spell: Spell
) -> None:
    await session.delete(spell)
    await session.commit()
