from sqlalchemy import String, Text, SmallInteger, Enum, UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from kingdom.models.base_model import Base
from kingdom.models.mixins.race import RaceRelationMixin
from kingdom.models.mixins.user import UserRelationMixin
from kingdom.models.mixins.character_class import CharacterClassMixin
from kingdom.models.mixins.god import GodMixin, DomainMixin
from kingdom.models.mixins.character import CharacterMixin
from kingdom.models.mixins.skill import SkillMixin
from kingdom.models.enum import MasteryLevels
if TYPE_CHECKING:
    from kingdom.models.inventory import (
        CharacterItem,
        CharacterCurrency,
        CharacterWorn,
        CharacterArmor,
        CharacterWeapon,
        EquippedItems
    )
    from kingdom.models.general import WeaponGroup


class Character(
    RaceRelationMixin,
    UserRelationMixin,
    CharacterClassMixin,
    GodMixin,
    DomainMixin,
    Base
):
    #mixins
    _user_back_populate = "characters"
    _race_back_populate = "characters"
    _character_class_back_populate = "characters"
    _god_back_populate = "characters"
    _domain_back_populate = "characters"
    _domain_id_nullable = True

    #fields
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100), nullable=True)
    alias: Mapped[str] = mapped_column(String(100), nullable=True)
    age: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    size: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    level: Mapped[int] = mapped_column(SmallInteger, default=1)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    #relations
    character_stats: Mapped[list["CharacterStat"]] = relationship(back_populates="character")
    character_points: Mapped[list["CharacterPoint"]] = relationship(back_populates='character')
    secondary_stats: Mapped[list["SecondaryStat"]] = relationship(back_populates="character")
    character_skill_masteries: Mapped[list["CharacterSkillMastery"]] = relationship(back_populates="character")
    character_weapon_masteries: Mapped[list["CharacterWeaponMastery"]] = relationship(back_populates='character')
    character_currencies: Mapped[list["CharacterCurrency"]] = relationship(back_populates='character')
    character_items: Mapped[list["CharacterItem"]] = relationship(back_populates='character')
    character_armors: Mapped[list["CharacterArmor"]] = relationship(back_populates='character')
    character_weapons: Mapped[list["CharacterWeapon"]] = relationship(back_populates='character')
    character_worns: Mapped[list["CharacterWorn"]] = relationship(back_populates='character')
    equipped_items: Mapped[list["EquippedItems"]] = relationship(back_populates='character')

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
    _character_id_unique = True

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
        return f"{self.__class__.__name__}(id={self.id}, name={self.character.__str__()!r}'s stats)"

    def __repr__(self):
        return self.character.__str__()


class CharacterPoint(CharacterMixin, Base):
    _character_back_populate = "character_points"
    _character_id_unique = True

    strength: Mapped[int] = mapped_column(SmallInteger, default=0)
    dexterity: Mapped[int] = mapped_column(SmallInteger, default=0)
    constitution: Mapped[int] = mapped_column(SmallInteger, default=0)
    intelligence: Mapped[int] = mapped_column(SmallInteger, default=0)
    wisdom: Mapped[int] = mapped_column(SmallInteger, default=0)
    charisma: Mapped[int] = mapped_column(SmallInteger, default=0)
    free: Mapped[int] = mapped_column(SmallInteger, default=0)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.character.__str__()!r}'s stat points)"

    def __repr__(self):
        return self.character.__str__()


class SecondaryStat(CharacterMixin, Base):
    _character_back_populate = "secondary_stats"
    _character_id_unique = True

    perception: Mapped[int] = mapped_column(SmallInteger, default=0)
    armor_class: Mapped[int] = mapped_column(SmallInteger, default=10)
    attack_class: Mapped[int] = mapped_column(SmallInteger, default=0)
    damage_bonus: Mapped[int] = mapped_column(SmallInteger, default=0)
    max_health: Mapped[int] = mapped_column(SmallInteger, default=1)
    health: Mapped[int] = mapped_column(SmallInteger, default=1)
    initiative: Mapped[int] = mapped_column(SmallInteger, default=0)
    fortitude_saving: Mapped[int] = mapped_column(SmallInteger, default=0)
    reflex_saving: Mapped[int] = mapped_column(SmallInteger, default=0)
    will_saving: Mapped[int] = mapped_column(SmallInteger, default=0)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s secondary stats)"

    def __repr__(self):
        return self.character.__str__()


class CharacterSkillMastery(CharacterMixin, SkillMixin, Base):
    __tablename__ = 'character_skill_masteries'
    __table_args__ = (
        UniqueConstraint(
            'character_id',
            'skill_id',
            name='idx_unique_character_skill_masteries'
        ),
    )

    _character_back_populate = 'character_skill_masteries'
    _character_id_unique = True
    _skill_back_populate = 'character_skill_masteries'

    mastery_level: Mapped[Enum] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.skill} mastery level)"

    def __repr__(self):
        return self.character.__str__()


class CharacterWeaponMastery(CharacterMixin, Base):
    __tablename__ = 'character_weapon_masteries'
    __table_args__ = (
        UniqueConstraint(
            'character_id',
            'weapon_group_id',
            name='idx_unique_character_weapon_masteries'
        ),
    )

    _character_back_populate = 'character_weapon_masteries'
    _character_id_unique = True

    weapon_group_id: Mapped[int] = mapped_column(
        ForeignKey(
            "weapon_groups.id", ondelete="CASCADE"
        )
    )
    weapon_group: Mapped["WeaponGroup"] = relationship(
        back_populates="character_weapon_masteries"
    )

    mastery_level: Mapped[Enum] = mapped_column(Enum(MasteryLevels), default=MasteryLevels.ABSENT)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.weapon} mastery level)"

    def __repr__(self):
        return self.character.__str__()
