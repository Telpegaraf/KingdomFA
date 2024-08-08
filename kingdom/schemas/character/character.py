from pydantic import BaseModel, ConfigDict
from typing import Annotated, Optional
from annotated_types import MaxLen

from kingdom.schemas.user import User
from kingdom.schemas.race import Race
from kingdom.schemas.character_class import CharacterClass
from kingdom.schemas.religion import God, Domain


class CharacterBase(BaseModel):
    first_name: Annotated[str, MaxLen(100)]
    last_name: Optional[Annotated[str, MaxLen(100)]]
    alias: Optional[Annotated[str, MaxLen(100)]]
    age: Optional[int]
    size: Optional[int]
    level: Optional[int] = 1
    description: Optional[str]
    user: User
    race: Race
    character_class: CharacterClass
    god: God
    domain: Optional[Domain]


class CharacterRead(BaseModel):
    first_name: Annotated[str, MaxLen(100)]
    last_name: Optional[Annotated[str, MaxLen(100)]]
    alias: Optional[Annotated[str, MaxLen(100)]]
    age: Optional[int]
    size: Optional[int]
    level: Optional[int] = 1
    description: Optional[str]
    user: User
    race: Race
    character_class: CharacterClass
    god: God
    domain: Optional[Domain]


class CharacterCreate(BaseModel):
    first_name: Annotated[str, MaxLen(100)]
    last_name: Optional[Annotated[str, MaxLen(100)]]
    alias: Optional[Annotated[str, MaxLen(100)]]
    age: Optional[int]
    size: Optional[int]
    level: Optional[int] = 1
    description: Optional[str]
    user_id: int
    race_id: int
    character_class_id: int
    god_id: int
    domain_id: Optional[int]


class CharacterUpdate(BaseModel):
    first_name: Annotated[str, MaxLen(100)]
    last_name: Optional[Annotated[str, MaxLen(100)]]
    alias: Optional[Annotated[str, MaxLen(100)]]
    age: Optional[int]
    size: Optional[int]
    level: Optional[int] = 1
    description: Optional[str]
    user_id: int
    race_id: int
    character_class_id: int
    god_id: int
    domain_id: Optional[int]


class CharacterName(BaseModel):
    first_name: Annotated[str, MaxLen(100)]
    last_name: Annotated[str, MaxLen(100)]
    alias: Annotated[str, MaxLen(100)]
    id: int


class Character(CharacterBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
