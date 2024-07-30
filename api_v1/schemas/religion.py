from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen


class DomainBase(BaseModel):
    name: Annotated[str, MaxLen(100)]


class DomainUpdate(DomainBase):
    name: str | None = None


class Domain(DomainBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class GodBase(BaseModel):
    name: Annotated[str, MaxLen(100)]
    alias: Annotated[str, MaxLen(100)]
    edict: Annotated[str, MaxLen(300)]
    anathema: Annotated[str, MaxLen(300)]
    areas_of_interest: Annotated[str, MaxLen(300)]
    temples: Annotated[str, MaxLen(300)]
    worship: Annotated[str, MaxLen(300)]
    sacred_animal: Annotated[str, MaxLen(300)]
    sacred_color: Annotated[str, MaxLen(300)]
    chosen_weapon: Annotated[str, MaxLen(300)]
    taro: Annotated[str, MaxLen(300)]
    alignment: Annotated[str, MaxLen(300)]
    domains: list[Domain]


class GodCreateUpdate(BaseModel):
    name: Annotated[str, MaxLen(100)]
    alias: Annotated[str, MaxLen(100)]
    edict: Annotated[str, MaxLen(300)]
    anathema: Annotated[str, MaxLen(300)]
    areas_of_interest: Annotated[str, MaxLen(300)]
    temples: Annotated[str, MaxLen(300)]
    worship: Annotated[str, MaxLen(300)]
    sacred_animal: Annotated[str, MaxLen(300)]
    sacred_color: Annotated[str, MaxLen(300)]
    chosen_weapon: Annotated[str, MaxLen(300)]
    taro: Annotated[str, MaxLen(300)]
    alignment: Annotated[str, MaxLen(300)]
    domains: list[int]


class God(GodBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
