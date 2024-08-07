from pydantic import BaseModel, ConfigDict
from annotated_types import Annotated, MaxLen, Optional
from kingdom.schemas.general import GeneralBase, GeneralDescriptionBase


class SpellBase(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: Annotated[str, MaxLen(1000)]
    level: int = 0
    spell_range: int = 0
    duration: Annotated[str, MaxLen(200)]
    sustain: bool = False
    ritual: bool = False
    secondary_casters: Optional[Annotated[str, MaxLen(200)]]
    cost: Optional[Annotated[str, MaxLen(200)]]
    target: Annotated[str, MaxLen(200)]
    source: Annotated[str, MaxLen(200)]
    spell_tradition: GeneralDescriptionBase
    spell_cast: GeneralBase
    spell_school: GeneralDescriptionBase
    spell_component: Optional[Annotated[str, MaxLen(200)]]
    spell_traits: Optional[list[GeneralDescriptionBase]]


class SpellRead(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: Annotated[str, MaxLen(1000)]
    level: int = 0
    spell_range: int = 0
    duration: Annotated[str, MaxLen(200)]
    sustain: bool = False
    ritual: bool = False
    secondary_casters: Optional[Annotated[str, MaxLen(200)]]
    cost: Optional[Annotated[str, MaxLen(200)]]
    target: Annotated[str, MaxLen(200)]
    source: Annotated[str, MaxLen(200)]
    spell_tradition: GeneralDescriptionBase
    spell_cast: GeneralBase
    spell_school: GeneralDescriptionBase
    spell_component: Optional[Annotated[str, MaxLen(200)]]
    spell_traits: Optional[list[GeneralDescriptionBase]]


class SpellCreate(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: Annotated[str, MaxLen(1000)]
    level: int = 0
    spell_range: int = 0
    duration: Annotated[str, MaxLen(200)]
    sustain: bool = False
    ritual: bool = False
    secondary_casters: Optional[Annotated[str, MaxLen(200)]]
    cost: Optional[Annotated[str, MaxLen(200)]]
    target: Annotated[str, MaxLen(200)]
    source: Annotated[str, MaxLen(200)]
    spell_tradition_id: int
    spell_cast_id: int
    spell_school_id: int
    spell_component: Optional[Annotated[str, MaxLen(200)]]
    spell_traits: Optional[list[int]]


class SpellUpdate(BaseModel):
    name: Annotated[str, MaxLen(200)]
    description: Annotated[str, MaxLen(1000)]
    level: int = 0
    spell_range: int = 0
    duration: Annotated[str, MaxLen(200)]
    sustain: bool = False
    ritual: bool = False
    secondary_casters: Optional[Annotated[str, MaxLen(200)]]
    cost: Optional[Annotated[str, MaxLen(200)]]
    target: Annotated[str, MaxLen(200)]
    source: Annotated[str, MaxLen(200)]
    spell_tradition_id: int
    spell_cast_id: int
    spell_school_id: int
    spell_component_id: Optional[Annotated[str, MaxLen(200)]]
    spell_traits: Optional[list[int]]


class Spell(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
