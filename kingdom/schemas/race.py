from pydantic import BaseModel, ConfigDict
from annotated_types import Annotated, MaxLen


class RaceBase(BaseModel):
    name: Annotated[str, MaxLen(50)]


class Race(RaceBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
