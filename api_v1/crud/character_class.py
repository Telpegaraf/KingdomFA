from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api_v1.schemas import character_class as schema
from api_v1.models import character_class as models
from database import db_helper


async def character_class_create(
        character_class_in: schema.CharacterClassBase,
        session: AsyncSession,
):
    print(character_class_in)
    character_class = models.CharacterClass(**character_class_in.model_dump())
    # character_class = models.CharacterClass(
    #     name = character_class_in.name,
    #     health_by_level = character_class_in.health_by_level,
    #     perception_mastery = character_class_in.perception_mastery,
    #     fortitude_mastery = character_class_in.fortitude_mastery,
    #     reflex_mastery = character_class_in.reflex_mastery,
    #     will_mastery = character_class_in.will_mastery,
    #     unarmed_mastery = character_class_in.unarmed_mastery,
    #     light_armor_mastery = character_class_in.light_armor_mastery,
    #     medium_armor_mastery = character_class_in.medium_armor_mastery,
    #     heavy_armor_mastery = character_class_in.heavy_armor_mastery
    # )
    session.add(character_class)
    await session.commit()
    await session.refresh(character_class)
    return character_class
