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
