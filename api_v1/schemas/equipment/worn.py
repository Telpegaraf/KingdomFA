from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated
from annotated_types import MaxLen
from api_v1.schemas.general import GeneralDescription


class Currency(BaseModel):
    name: Annotated[str, MaxLen(200)]
    price: int
    description: str
    weight: Decimal


class CurrencyBase(Currency):
    model_config = ConfigDict(from_attributes=True)

    id: int


class SlotBase(BaseModel):
    slot: Annotated[str, MaxLen(100)]
    limit: bool


class Slot(SlotBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class WornBase(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    price: int
    weight: Decimal
    slot: Slot
    level: int = Field(..., ge=1, le=1)
    activate: str
    effect: str
    worn_traits: list[GeneralDescription]
    currency: Currency


class WornCreate(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    price: int
    weight: Decimal
    slot_id: int
    level: int = Field(..., ge=1, le=1)
    activate: str
    effect: str
    worn_traits: list[int]
    currency_id: int


class Worn(WornBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

