from sqlalchemy import String, SmallInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base_model import Base

from core.models.associations.spell_trait_association import SpellTraitAssociation
from core.models.mixins.spell import (
    SpellTraditionMixin,
    SpellCastMixin,
    SpellSchoolMixin,
)

if TYPE_CHECKING:
    from core.models.general import (
        SpellTrait,
    )


class Spell(
    SpellTraditionMixin,
    SpellCastMixin,
    SpellSchoolMixin,
    Base
):
    _spell_tradition_back_populate = "spells"
    _spell_cast_back_populate = "spells"
    _spell_school_back_populate = "spells"

    name: Mapped[str] = mapped_column(String(200), unique=True)
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
    spell_component: Mapped[str] = mapped_column(String(200), nullable=True)

    spell_traits: Mapped[list["SpellTrait"]] = relationship(
        secondary='spell_trait_association',
        back_populates='spells'
    )
    spell_trait_details: Mapped[list["SpellTraitAssociation"]] = relationship(
        back_populates='spell', cascade="all, delete-orphan"
    )
