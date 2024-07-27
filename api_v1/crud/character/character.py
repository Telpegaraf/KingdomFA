from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api_v1.schemas.character.character import CharacterCreate, CharacterUpdate
from api_v1.models.character import Character
from api_v1.models.user import User
from api_v1.models.religion import God, Domain
from api_v1.models.race import Race
from api_v1.models.character_class import CharacterClass


async def character_detail(session: AsyncSession, character_id: int) -> Character:
    return await session.scalar(
        select(Character).
        where(Character.id == character_id).options(
            selectinload(Character.race),
            selectinload(Character.character_class),
            selectinload(Character.god).selectinload(God.domains),
            selectinload(Character.domain),
            selectinload(Character.user),
        )
    )


async def character_list(session: AsyncSession) -> list[Character]:
    stmt = select(Character).options(
        selectinload(Character.race),
        selectinload(Character.character_class),
        selectinload(Character.god).selectinload(God.domains),
        selectinload(Character.domain),
        selectinload(Character.user),
    ).order_by(Character.id)
    result: Result = await session.execute(stmt)
    characters = result.scalars().all()
    return list(characters)


async def character_create(
        session: AsyncSession,
        character_in: CharacterCreate,
) -> Character:
    user_result = await session.execute(
        select(User).where(User.id == character_in.user_id)
    )
    user = user_result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User is not found")
    race_result = await session.execute(
        select(Race).where(Race.id == character_in.race_id)
    )
    race = race_result.scalar_one_or_none()
    if race is None:
        raise HTTPException(status_code=404, detail="Race is not found")
    character_class_result = await session.execute(
        select(CharacterClass).where(CharacterClass.id == character_in.character_class_id)
    )
    character_class = character_class_result.scalar_one_or_none()
    if character_class is None:
        raise HTTPException(status_code=404, detail="Character Class is not found")
    god_result = await session.execute(
        select(God).where(God.id == character_in.god_id)
    )
    god = god_result.scalar_one_or_none()
    if god is None:
        raise HTTPException(status_code=404, detail="God is not found")
    domain_result = await session.execute(
        select(Domain).where(Domain.id == character_in.domain_id)
    )
    domain = domain_result.scalar_one_or_none()
    if domain is None:
        raise HTTPException(status_code=404, detail="Domain is not found")
    character = Character(
        first_name=character_in.first_name,
        last_name=character_in.last_name,
        alias=character_in.alias,
        size=character_in.size,
        age=character_in.age,
        level=character_in.age,
        description=character_in.description,
        race=race,
        character_class=character_class,
        god=god,
        domain=domain,
        user=user
    )
    session.add(character)
    await session.commit()
    await session.refresh(character)
    return await character_detail(session=session, character_id=character.id)


async def character_update(
        session: AsyncSession,
        character_update: CharacterUpdate,
        character: Character
) -> Character:
    user_result = await session.execute(
        select(User).where(User.id == character_update.user_id)
    )
    user = user_result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User is not found")
    race_result = await session.execute(
        select(Race).where(Race.id == character_update.race_id)
    )
    race = race_result.scalar_one_or_none()
    if race is None:
        raise HTTPException(status_code=404, detail="Race is not found")
    character_class_result = await session.execute(
        select(CharacterClass).where(CharacterClass.id == character_update.character_class_id)
    )
    character_class = character_class_result.scalar_one_or_none()
    if character_class is None:
        raise HTTPException(status_code=404, detail="Character Class is not found")
    god_result = await session.execute(
        select(God).where(God.id == character_update.god_id)
    )
    god = god_result.scalar_one_or_none()
    if god is None:
        raise HTTPException(status_code=404, detail="God is not found")
    domain_result = await session.execute(
        select(Domain).where(Domain.id == character_update.domain_id)
    )
    domain = domain_result.scalar_one_or_none()
    if domain is None:
        raise HTTPException(status_code=404, detail="Domain is not found")
    for key, value in character_update.model_dump(exclude_unset=True).items():
        if hasattr(character, key) and key not in [
            "user_id", "race_id", "character_class_id", "god_id", "domain_id"
        ]:
            setattr(character, key, value)
    character.race = race
    character.character_class = character_class
    character.god = god
    character.dom = domain
    character.user = user
    await session.commit()
    await session.refresh(character)
    return character


async def character_delete(
        session: AsyncSession,
        character: Character
) -> None:
    await session.delete(character)
    await session.commit()
