from pydantic import BaseModel, ConfigDict, PositiveFloat
from kingdom.schemas.equipment.currency import Currency
from typing import Annotated
from annotated_types import MaxLen


class ItemBase(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    price: int
    weight: PositiveFloat
    currency: Currency


class ItemRead(ItemBase):
    pass


class ItemCreateUpdate(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: str
    price: int
    weight: PositiveFloat
    currency_id: int


class Item(ItemBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
