from pydantic import BaseModel, ConfigDict
from api_v1.schemas.character.character import CharacterName
from api_v1.schemas.general import GeneralDescription
from api_v1.models.enum import MasteryLevels


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
