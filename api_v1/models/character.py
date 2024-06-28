from sqlalchemy import String, Text, SmallInteger, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api_v1.models.base_model import Base
from api_v1.models.mixins.race import RaceRelationMixin
from api_v1.models.mixins.user import UserRelationMixin
from api_v1.models.mixins.character_class import CharacterClassMixin
from api_v1.models.mixins.god import GodMixin, DomainMixin
from api_v1.models.mixins.character import CharacterMixin
from api_v1.models.enum import MasteryLevels


class Character(
    RaceRelationMixin,
    UserRelationMixin,
    CharacterClassMixin,
    GodMixin,
    DomainMixin,
    Base
):
    _user_back_populate = "characters"
    _race_back_populate = "characters"
    _character_class_back_populate = "characters"
    _god_back_populate = "characters"
    _domain_back_populate = "characters"
    _domain_id_nullable = True
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100), nullable=True)
    alias: Mapped[str] = mapped_column(String(100), nullable=True)
    age: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    size: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    level: Mapped[int] = mapped_column(SmallInteger, default=1)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    character_stats: Mapped[list["CharacterStat"]] = relationship(back_populates="character")

    def __str__(self):
        name = self.first_name
        if self.last_name:
            name += f" {self.last_name}"
        if self.alias:
            name += f" {self.alias}"

        return f"{self.__class__.__name__}(id={self.id}, name={name!r})"

    def __repr__(self):
        return self.__str__()


class CharacterStat(CharacterMixin, Base):
    _character_back_populate = "character_stats"

    strength: Mapped[int] = mapped_column(SmallInteger, default=10)
    dexterity: Mapped[int] = mapped_column(SmallInteger, default=10)
    constitution: Mapped[int] = mapped_column(SmallInteger, default=10)
    intelligence: Mapped[int] = mapped_column(SmallInteger, default=10)
    wisdom: Mapped[int] = mapped_column(SmallInteger, default=10)
    charisma: Mapped[int] = mapped_column(SmallInteger, default=10)
    max_speed: Mapped[int] = mapped_column(SmallInteger, default=30)
    speed: Mapped[int] = mapped_column(SmallInteger, default=30)
    perception_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    unarmed_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    light_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    medium_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    heavy_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    fortitude_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    reflex_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)
    will_armor_mastery: Mapped[MasteryLevels] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.character.__str__()!r})"

    def __repr__(self):
        return self.character.__str__()
