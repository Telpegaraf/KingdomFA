from pydantic import BaseModel, ConfigDict
from api_v1.models.enum import MasteryLevels
from api_v1.schemas.character.character import CharacterName


class CharacterStatsBase(BaseModel):
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    max_speed: int = 30
    speed: int = 30
    perception_mastery: MasteryLevels = MasteryLevels.ABSENT
    unarmed_mastery: MasteryLevels = MasteryLevels.ABSENT
    light_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    medium_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    heavy_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    fortitude_mastery: MasteryLevels = MasteryLevels.ABSENT
    reflex_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    will_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    character: CharacterName


class CharacterStatsRead(CharacterStatsBase):
    pass


class CharacterStatsCreate(BaseModel):
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    max_speed: int = 30
    speed: int = 30
    perception_mastery: MasteryLevels = MasteryLevels.ABSENT
    unarmed_mastery: MasteryLevels = MasteryLevels.ABSENT
    light_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    medium_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    heavy_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    fortitude_mastery: MasteryLevels = MasteryLevels.ABSENT
    reflex_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    will_armor_mastery: MasteryLevels = MasteryLevels.ABSENT
    character_id: int


class CharacterStatsUpdate(CharacterStatsCreate):
    pass


class CharacterStats(CharacterStatsBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
