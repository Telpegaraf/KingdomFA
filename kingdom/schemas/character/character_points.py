from pydantic import BaseModel, ConfigDict
from kingdom.schemas.character.character import CharacterName


class CharacterPointBase(BaseModel):
    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0
    free: int = 0
    character: CharacterName


class CharacterPointRead(CharacterPointBase):
    pass


class CharacterPointCreate(BaseModel):
    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0
    free: int = 0
    character_id: int


class CharacterPointUpdate(CharacterPointCreate):
    pass


class CharacterPoint(CharacterPointBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    