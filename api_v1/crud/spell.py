from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.schemas.spell import SpellCreate, SpellUpdate
from core.models.spell import Spell
from core.models.general import SpellCast, SpellTrait, SpellSchool, SpellTradition
from api_v1.utils.model_result import get_model_result, get_model_m2m_result


async def spell_detail(session: AsyncSession, spell_id: int) -> Spell:
    return await session.scalar(
        select(Spell).
        where(Spell.id == spell_id).options(
            selectinload(Spell.spell_traits),
            selectinload(Spell.spell_school),
            selectinload(Spell.spell_cast),
            selectinload(Spell.spell_tradition),
        )
    )


async def spell_list(session: AsyncSession) -> list[Spell]:
    stmt = select(Spell).options(
            selectinload(Spell.spell_traits),
            selectinload(Spell.spell_school),
            selectinload(Spell.spell_cast),
            selectinload(Spell.spell_tradition),
        ).order_by(Spell.id)
    result: Result = await session.execute(stmt)
    spells = result.scalars().all()
    return list(spells)


async def spell_create(
        session: AsyncSession,
        spell_in: SpellCreate,
) -> Spell:
    spell_cast = await get_model_result(model=SpellCast, object_id=spell_in.spell_cast_id, session=session)
    spell_tradition = await get_model_result(model=SpellTradition,
                                             object_id=spell_in.spell_tradition_id, session=session)
    spell_school = await get_model_result(model=SpellSchool, object_id=spell_in.spell_school_id, session=session)
    existing_spell_traits = await get_model_m2m_result(model=SpellTrait,
                                                       object_list=spell_in.spell_traits, session=session)
    spell_data = spell_in.dict(exclude={"spell_cast_id", "spell_tradition_id", "spell_school_id", "spell_traits"})

    spell = Spell(
        **spell_data,
        spell_cast=spell_cast,
        spell_tradition=spell_tradition,
        spell_school=spell_school,
        spell_traits=existing_spell_traits
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
    spell_cast = await get_model_result(model=SpellCast, object_id=spell_update.spell_cast_id, session=session)
    spell_tradition = await get_model_result(model=SpellTradition,
                                             object_id=spell_update.spell_tradition_id, session=session)
    spell_school = await get_model_result(model=SpellSchool, object_id=spell_update.spell_school_id, session=session)
    existing_spell_traits = await get_model_m2m_result(model=SpellTrait,
                                                       object_list=spell_update.spell_traits, session=session)
    for key, value in spell_update.model_dump(exclude_unset=True).items():
        if hasattr(spell, key) and key not in [
            "spell_cast_id", "spell_tradition_id",
            "spell_school_id", "spell_traits",
        ]:
            setattr(spell, key, value)
    spell.spell_cast = spell_cast
    spell.spell_tradition = spell_tradition
    spell.spell_school = spell_school
    spell.spell_traits.clear()
    for value in existing_spell_traits:
        spell.spell_traits.append(value)
    await session.commit()
    await session.refresh(spell)
    return spell


async def spell_delete(
        session: AsyncSession,
        spell: Spell
) -> None:
    await session.delete(spell)
    await session.commit()
