from pydantic import BaseModel, ConfigDict
from kingdom.schemas.character.character import CharacterName


class SecondaryStatBase(BaseModel):
    perception: int = 0
    armor_class: int = 0
    attack_class: int = 0
    damage_bonus: int = 0
    max_health: int = 0
    health: int = 0
    initiative: int = 0
    fortitude_saving: int
    reflex_saving: int
    will_saving: int
    character: CharacterName


class SecondaryStatRead(SecondaryStatBase):
    pass


class SecondaryStatCreate(BaseModel):
    perception: int = 0
    armor_class: int = 0
    attack_class: int = 0
    damage_bonus: int = 0
    max_health: int = 0
    health: int = 0
    initiative: int = 0
    fortitude_saving: int
    reflex_saving: int
    will_saving: int
    character_id: int


class SecondaryStatUpdate(SecondaryStatCreate):
    pass


class SecondaryStat(SecondaryStatBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
