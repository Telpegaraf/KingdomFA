from sqlalchemy import ForeignKey, String, SmallInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from api_v1.models.base_model import Base

from api_v1.models.mixins.spell import (
    SpellTraditionMixin,
    SpellComponentMixin,
    SpellCastMixin,
    SpellSchoolMixin,
    SpellTraitMixin
)

if TYPE_CHECKING:
    from api_v1.models.general import (
        SpellCast,
        SpellTrait,
        SpellSchool,
        SpellComponent
    )


class Spell(
    SpellTraditionMixin,
    SpellComponentMixin,
    SpellCastMixin,
    SpellSchoolMixin,
    SpellTraitMixin,
    Base
):
    _spell_tradition_back_populate = "spells"
    _spell_component_back_populate = "spells"
    _spell_component_id_nullable = True
    _spell_cast_back_populate = "spells"
    _spell_school_back_populate = "spells"
    _spell_trait_back_populate = "spells"
    _spell_trait_id_nullable = True

    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(1000))
    level: Mapped[str] = mapped_column(SmallInteger, default=0)
    spell_range: Mapped[int] = mapped_column(SmallInteger, default=0)
    duration: Mapped[str] = mapped_column(String(200))
    sustain: Mapped[bool] = mapped_column(Boolean, default=False)
    ritual: Mapped[bool] = mapped_column(Boolean, default=False)
    secondary_casters: Mapped[str] = mapped_column(String(200), nullable=True)
    cost: Mapped[str] = mapped_column(String(200), nullable=True)
    target: Mapped[str] = mapped_column(String(200))
    source: Mapped[str] = mapped_column(String(200))

    #TODO Trait and Component => M2m
