from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen
from api_v1.models.enum import HealthByLevel, MasteryLevels


class CharacterClassBase(BaseModel):
    name: Annotated[str, MaxLen(120)]
    health_by_level: HealthByLevel
    perception_mastery: MasteryLevels
    fortitude_mastery: MasteryLevels
    reflex_mastery: MasteryLevels
    will_mastery: MasteryLevels
    unarmed_mastery: MasteryLevels
    light_armor_mastery: MasteryLevels
    medium_armor_mastery: MasteryLevels
    heavy_armor_mastery: MasteryLevels


class CharacterClass(CharacterClassBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
