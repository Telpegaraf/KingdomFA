from pydantic import BaseModel, ConfigDict
from kingdom.schemas.character.character import CharacterName
from kingdom.schemas.general import GeneralDescription
from kingdom.models.enum import MasteryLevels


class CharacterSkillMasteryBase(BaseModel):
    mastery_level: MasteryLevels = MasteryLevels.ABSENT
    skill: GeneralDescription
    character: CharacterName


class CharacterSkillMasteryRead(CharacterSkillMasteryBase):
    pass


class CharacterSkillMasteryCreate(BaseModel):
    mastery_level: MasteryLevels = MasteryLevels.ABSENT
    skill_id: int
    character_id: int


class CharacterSkillMasteryUpdate(CharacterSkillMasteryCreate):
    pass


class CharacterSkillMastery(CharacterSkillMasteryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
