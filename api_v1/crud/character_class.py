from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from api_v1.schemas import character_class as schema
from api_v1.models import character_class as models


async def character_class_create(
        character_class_in: schema.CharacterClassBase,
        session: AsyncSession,
):
    character_class = models.CharacterClass(**character_class_in.model_dump())
    session.add(character_class)
    await session.commit()
    await session.refresh(character_class)
    return character_class


async def character_class_list(
        session: AsyncSession
):
    stmt = select(models.CharacterClass).order_by(models.CharacterClass.id)
    result: Result = await session.execute(stmt)
    character_classes = result.scalars().all()
    return list(character_classes)


async def character_class_update(
        character_class_update: schema.CharacterClassBase,
        character_class: models.CharacterClass,
        session: AsyncSession
):
    for name, value in character_class_update.model_dump(exclude_unset=True).items():
        setattr(character_class, name, value)
    await session.commit()
    return character_class


async def character_class_delete(
        character_class: models.CharacterClass,
        session: AsyncSession
) -> None:
    await session.delete(character_class)
    await session.commit()
