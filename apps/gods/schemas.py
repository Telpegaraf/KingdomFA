from pydantic import BaseModel, Field
from typing import List


class DomainBase(BaseModel):
    name: str


class Domain(DomainBase):
    id: int

    class Config:
        from_attributes = True


class GodBase(BaseModel):
    name: str
    alias: str
    edict: str
    anathema: str
    areas_of_interest: str
    temples: str
    worship: str
    sacred_animal: str
    sacred_color: str
    chosen_weapon: str
    taro: str
    alignment: str


class God(GodBase):
    id: int
    domain: List[Domain] = Field(default_factory=list)

    class Config:
        from_attributes = True
