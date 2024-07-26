from pydantic import BaseModel, ConfigDict
from typing import Annotated, Optional
from annotated_types import MaxLen

from api_v1.schemas.user import User


class CharacterBase(BaseModel):
    first_name: Annotated[str, MaxLen(100)]
    last_name: Optional[Annotated[str, MaxLen(100)]]
    alias: Optional[Annotated[str, MaxLen(100)]]
    age: Optional[int]
    size: Optional[int]
    level: Optional[int] = 1
    description: Optional[str]
    user: User
    #race: R


class Character(CharacterBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
