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
from api_v1.utils.model_result import get_model_result
import logging

logger = logging.getLogger()


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
        payload: dict
) -> Character:
    print(payload)
    logger.warning(payload)
    user = await get_model_result(model=User, object_id=character_in.user_id, session=session)
    race = await get_model_result(model=Race, object_id=character_in.race_id, session=session)
    character_class = await get_model_result(model=CharacterClass, object_id=character_in.character_class_id,
                                             session=session)
    god = await get_model_result(model=God, object_id=character_in.god_id, session=session)
    domain = await get_model_result(model=Domain, object_id=character_in.domain_id, session=session)\
        if character_in.domain_id else None

    character_data = character_in.dict(exclude={"user_id", "race_id", "character_class_id", "god_id", "domain_id"})

    character = Character(
        **character_data,
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
    user = await get_model_result(model=User, object_id=character_update.user_id, session=session)
    race = await get_model_result(model=Race, object_id=character_update.race_id, session=session)
    character_class = await get_model_result(model=CharacterClass, object_id=character_update.character_class_id,
                                             session=session)
    god = await get_model_result(model=God, object_id=character_update.god_id, session=session)
    domain = await get_model_result(model=Domain, object_id=character_update.domain_id, session=session) \
        if character_update.domain_id else None
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
