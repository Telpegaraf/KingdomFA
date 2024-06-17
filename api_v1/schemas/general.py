from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MaxLen


class GeneralBase(BaseModel):
    name: Annotated[str, MaxLen(100)]


class GeneralDescriptionBase(GeneralBase):
    description: Annotated[str, MaxLen(300)]


class General(GeneralBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class GeneralDescription(GeneralDescriptionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
