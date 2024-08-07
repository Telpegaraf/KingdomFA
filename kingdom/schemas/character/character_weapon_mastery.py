from pydantic import BaseModel, ConfigDict
from kingdom.schemas.character.character import CharacterName
from kingdom.schemas.general import GeneralDescriptionBase
from kingdom.models.enum import MasteryLevels


class CharacterWeaponMasteryBase(BaseModel):
    mastery_level: MasteryLevels = MasteryLevels.ABSENT
    weapon_group: GeneralDescriptionBase
    character: CharacterName


class CharacterWeaponMasteryRead(CharacterWeaponMasteryBase):
    pass


class CharacterWeaponMasteryCreate(BaseModel):
    mastery_level: MasteryLevels = MasteryLevels.ABSENT
    weapon_group_id: int
    character_id: int


class CharacterWeaponMasteryUpdate(CharacterWeaponMasteryCreate):
    pass


class CharacterWeaponMastery(CharacterWeaponMasteryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
