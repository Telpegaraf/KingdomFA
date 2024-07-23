from pydantic import BaseModel, PositiveFloat, ConfigDict, Field
from typing import Annotated
from annotated_types import MaxLen
from api_v1.schemas.equipment.currency import Currency
from api_v1.schemas.general import General, GeneralDescription
from api_v1.models.equipment import ArmorCategory


# _____________________________
# schemas for model(ArmorGroup)
class ArmorGroupBase(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: Annotated[str, MaxLen(500)]
    hardness: int
    health: int
    broken_threshold: int


class ArmorGroup(ArmorGroupBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


# _________________________
# schemas for model (Armor)
class ArmorBase(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    price: int
    weight: PositiveFloat
    ac_bonus: int
    dexterity_modifier_cap: int
    check_penalty: bool
    speed_penalty: bool
    strength: int
    level: int
    currency: Currency
    armor_group: ArmorGroup
    armor_traits: list[GeneralDescription]
    armor_specializations: list[GeneralDescription]
    category: ArmorCategory


class ArmorRead(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    price: int
    weight: PositiveFloat
    ac_bonus: int
    dexterity_modifier_cap: int
    check_penalty: bool
    speed_penalty: bool
    strength: int
    level: int = Field(..., ge=1, le=20)
    currency: Currency
    armor_group: ArmorGroup
    armor_traits: list[GeneralDescription]
    armor_specializations: list[GeneralDescription]
    category: ArmorCategory


class ArmorCreate(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    price: int
    weight: PositiveFloat
    ac_bonus: int
    dexterity_modifier_cap: int
    check_penalty: bool
    speed_penalty: bool
    strength: int
    level: int = Field(..., ge=1, le=20)
    currency_id: int
    armor_group_id: int
    armor_traits: list[int]
    armor_specializations: list[int]
    category: ArmorCategory


class Armor(ArmorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

