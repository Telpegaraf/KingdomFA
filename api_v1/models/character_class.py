from sqlalchemy import String, SmallInteger, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from api_v1.models.base_model import Base
from api_v1.models.enum import MasteryLevels, HealthByLevel
from api_v1.models.mixins.spell import SpellTraditionMixin
from api_v1.models.mixins.feat import FeatMixin
from api_v1.models.mixins.character_class import CharacterClassMixin

if TYPE_CHECKING:
    from api_v1.models.feat import Feat


class CharacterClass(SpellTraditionMixin, Base):
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

    feats: Mapped[list["Feat"]] = relationship(back_populates="character_class")
    features: Mapped[list["Feature"]] = relationship(back_populates="character_class")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name


class Background(FeatMixin, Base):
    _feat_back_populate = "backgrounds"
    _feat_id_nullable = True

    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(200))


class Feature(FeatMixin, CharacterClassMixin, Base):
    _character_class_back_populate = "features"
    _feat_back_populate = "features"
    _feat_id_nullable = True

    level: Mapped[int] = mapped_column(SmallInteger, default=1)
    class_feat_count: Mapped[int] = mapped_column(SmallInteger, default=0)
    general_feat_count: Mapped[int] = mapped_column(SmallInteger, default=0)
    background_feat_count: Mapped[int] = mapped_column(SmallInteger, default=0)
    skill_count: Mapped[int] = mapped_column(SmallInteger, default=0)
    stats_boost:Mapped[int] = mapped_column(SmallInteger, default=0)
