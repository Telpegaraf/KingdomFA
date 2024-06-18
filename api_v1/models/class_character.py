from sqlalchemy import String, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column

from api_v1.models.base_model import Base
from api_v1.models.enum import MasteryLevels
from api_v1.models.mixins.spell_tradition import SpellTraditionRelationMixin


class CharacterClass(SpellTraditionRelationMixin, Base):
    _spell_tradition_back_populate = "character_classes"
    _spell_tradition_id_nullable = True
    name: Mapped[str] = mapped_column(String(120))
    health_by_level: Mapped[int] = mapped_column(Integer)
    perception_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels))
    fortitude_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels))
    reflex_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels))
    will_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels))
    unarmed_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels))
    light_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels))
    medium_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels))
    heavy_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name

