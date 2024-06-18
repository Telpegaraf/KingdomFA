from sqlalchemy import String, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column

from api_v1.models.base_model import Base
from api_v1.models.enum import MasteryLevels, HealthByLevel
from api_v1.models.mixins.spell_tradition import SpellTraditionRelationMixin


class CharacterClass(SpellTraditionRelationMixin, Base):
    _spell_tradition_back_populate = "character_classes"
    _spell_tradition_id_nullable = True
    name: Mapped[str] = mapped_column(String(120), unique=True)
    health_by_level: Mapped[HealthByLevel] = mapped_column(Enum(HealthByLevel), default=HealthByLevel.SIX)
    perception_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    fortitude_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    reflex_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    will_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    unarmed_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    light_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    medium_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    heavy_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name

