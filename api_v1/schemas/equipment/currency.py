from pydantic import BaseModel, PositiveFloat, ConfigDict
from typing import Annotated
from annotated_types import MaxLen


class CurrencyBase(BaseModel):
    name: Annotated[str, MaxLen(200)]
    price: int
    description: str
    weight: PositiveFloat


class Currency(CurrencyBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
