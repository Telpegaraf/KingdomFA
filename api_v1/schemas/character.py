from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen


class CharacterBase(BaseModel):
    first_name: Annotated[str, MaxLen(100)]
    last_name: Annotated[str, MaxLen(100)]
    alias: Annotated[str, MaxLen(100)]
    age: int
    level: int
    description: str


class Character(CharacterBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
