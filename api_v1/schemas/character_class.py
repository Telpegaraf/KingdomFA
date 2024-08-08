from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen
from core.models.enum import HealthByLevel, MasteryLevels
from core.models.general import SpellTradition


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
    spell_tradition_id: Annotated[int, SpellTradition] | None = None


class CharacterClass(CharacterClassBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
