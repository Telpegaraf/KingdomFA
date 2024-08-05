from pydantic import BaseModel, ConfigDict, Field
from api_v1.schemas.character.character import CharacterName
from api_v1.schemas.equipment.currency import Currency
from api_v1.schemas.equipment.weapon import Weapon
from api_v1.schemas.equipment.armor import Armor
from api_v1.schemas.equipment.worn import Worn
from api_v1.schemas.equipment.item import Item


class CharacterCurrencyBase(BaseModel):
    character: CharacterName
    currency: Currency
    quantity: int


class CharacterCurrencyRead(CharacterCurrencyBase):
    pass


class CharacterCurrencyCreateUpdate(BaseModel):
    character_id: int
    currency_id: int
    quantity: int = Field(..., ge=1)


class CharacterCurrency(CharacterCurrencyBase):
    model_config = ConfigDict(from_attributes=True)


class CharacterWeaponBase(BaseModel):
    character: CharacterName
    weapon: Weapon
    quantity: int


class CharacterWeaponRead(CharacterWeaponBase):
    pass


class CharacterWeaponCreateUpdate(BaseModel):
    character_id: int
    weapon_id: int
    quantity: int = Field(..., ge=1)


class CharacterWeapon(CharacterWeaponBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class CharacterArmorBase(BaseModel):
    character: CharacterName
    armor: Armor
    quantity: int


class CharacterArmorRead(CharacterArmorBase):
    pass


class CharacterArmorCreateUpdate(BaseModel):
    character_id: int
    armor_id: int
    quantity: int = Field(..., ge=1)


class CharacterArmor(CharacterArmorBase):
    model_config = ConfigDict(from_attributes=True)


class CharacterWornBase(BaseModel):
    character: CharacterName
    worn: Worn
    quantity: int


class CharacterWornRead(CharacterWornBase):
    pass


class CharacterWornCreateUpdate(BaseModel):
    character_id: int
    worn_id: int
    quantity: int = Field(..., ge=1)


class CharacterWorn(CharacterWornBase):
    model_config = ConfigDict(from_attributes=True)


class CharacterItemBase(BaseModel):
    character: CharacterName
    item: Item
    quantity: int


class CharacterItemRead(CharacterItemBase):
    pass


class CharacterItemCreateUpdate(BaseModel):
    character_id: int
    item_id: int
    quantity: int = Field(..., ge=1)


class CharacterItem(CharacterItemBase):
    model_config = ConfigDict(from_attributes=True)

