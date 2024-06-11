from pydantic import BaseModel, Field, ConfigDict
from typing import List, Annotated
from annotated_types import MaxLen


class DomainBase(BaseModel):
    name: Annotated[str, MaxLen(100)]


class DomainUpdate(DomainBase):
    name: str | None = None


class Domain(DomainBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

#
#
#
# class GodBase(BaseModel):
#     name: str
#     alias: str
#     edict: str
#     anathema: str
#     areas_of_interest: str
#     temples: str
#     worship: str
#     sacred_animal: str
#     sacred_color: str
#     chosen_weapon: str
#     taro: str
#     alignment: str
#
#
# class God(GodBase):
#     id: int
#     domain: List[Domain] = Field(default_factory=list)
#
#     class Config:
#         from_attributes = True
