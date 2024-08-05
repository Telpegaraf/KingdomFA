from pydantic import BaseModel, ConfigDict
from api_v1.schemas.character.character import Character
from api_v1.schemas.equipment.currency import Currency
from api_v1.schemas.equipment.weapon import Weapon
from api_v1.schemas.equipment.armor import Armor
from api_v1.schemas.equipment.worn import Worn
from api_v1.schemas.equipment.item import Item


class CharacterCurrencyBase(BaseModel):
    character: Character
    currency: Currency
    quantity: int


class CharacterCurrencyRead(CharacterCurrencyBase):
    pass


class CharacterCurrencyCreateUpdate(BaseModel):
    character_id: int
    currency: int
    quantity: int


class CharacterCurrency(CharacterCurrencyBase):
    model_config = ConfigDict(from_attributes=True)


class CharacterWeaponBase(BaseModel):
    character: Character
    weapon: Weapon
    quantity: int


class CharacterWeaponRead(CharacterWeaponBase):
    pass


class CharacterWeaponCreateUpdate(BaseModel):
    character_id: int
    weapon_id: int
    quantity: int


class CharacterWeapon(CharacterWeaponBase):
    model_config = ConfigDict(from_attributes=True)


class CharacterArmorBase(BaseModel):
    character: Character
    armor: Armor
    quantity: int


class CharacterArmorRead(CharacterArmorBase):
    pass


class CharacterArmorCreateUpdate(BaseModel):
    character_id: int
    armor_id: int
    quantity: int


class CharacterArmor(CharacterArmorBase):
    model_config = ConfigDict(from_attributes=True)


class CharacterWornBase(BaseModel):
    character: Character
    worn: Worn
    quantity: int


class CharacterWornRead(CharacterWornBase):
    pass


class CharacterWornCreateUpdate(BaseModel):
    character_id: int
    worn_id: int
    quantity: int


class CharacterWorn(CharacterWornBase):
    model_config = ConfigDict(from_attributes=True)


class CharacterItemBase(BaseModel):
    character: Character
    item: Item
    quantity: int


class CharacterItemRead(CharacterCurrencyBase):
    pass


class CharacterItemCreateUpdate(BaseModel):
    character_id: int
    item_id: int
    quantity: int


class CharacterItem(CharacterCurrencyBase):
    model_config = ConfigDict(from_attributes=True)

