from pydantic import BaseModel, ConfigDict
from typing import Annotated, Optional
from annotated_types import MaxLen

from api_v1.schemas.user import User
from api_v1.schemas.race import Race
from api_v1.schemas.character_class import CharacterClass
from api_v1.schemas.religion import God, Domain


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
    user_id: [int]
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
    user_id: [int]
    race_id: int
    character_class_id: int
    god_id: int
    domain_id: Optional[int]


class Character(CharacterBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
