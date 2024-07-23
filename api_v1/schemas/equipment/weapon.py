from annotated_types import MaxLen
from pydantic import BaseModel, Field, PositiveFloat, ConfigDict
from typing import Annotated, Optional
from api_v1.models.equipment import Dice, Currency
from api_v1.models.general import GeneralDescriptionBase


class WeaponBase(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    damage_type_id: int
    second_damage_type_id: Optional[int] = None
    dice: Dice
    dice_count: int
    bonus_damage: int
    second_dice: Dice
    second_dice_count: Optional[int] = None
    second_bonus_damage: Optional[int] = None
    range: Optional[int] = None
    reload: Optional[int] = None
    two_hands: bool = False
    level: int = Field(ge=0, le=20, default=1)
    weapon_group_id: Optional[list[GeneralDescriptionBase]] = None
    weapon_specialization_id: Optional[list[GeneralDescriptionBase]] = None
    currency_id: Currency
    price: int
    weight: PositiveFloat


class WeaponCreate(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    damage_type_id: int
    second_damage_type_id: Optional[int] = None
    dice: Dice
    dice_count: int
    bonus_damage: int
    second_dice: Dice
    second_dice_count: Optional[int] = None
    second_bonus_damage: Optional[int] = None
    range: Optional[int] = None
    reload: Optional[int] = None
    two_hands: bool = False
    level: int = Field(ge=0, le=20, default=1)
    weapon_group_id: Optional[list[int]] = None
    weapon_specialization_id: Optional[list[int]] = None
    currency_id: int
    price: int
    weight: PositiveFloat


class WeaponUpdate(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    damage_type_id: int
    second_damage_type_id: Optional[int] = None
    dice: Dice
    dice_count: int
    bonus_damage: int
    second_dice: Dice
    second_dice_count: Optional[int] = None
    second_bonus_damage: Optional[int] = None
    range: Optional[int] = None
    reload: Optional[int] = None
    two_hands: bool = False
    level: int = Field(ge=0, le=20, default=1)
    weapon_group_id: Optional[int] = None
    weapon_specialization_id: Optional[int] = None
    currency_id: int
    price: int
    weight: PositiveFloat


class Weapon(WeaponBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
