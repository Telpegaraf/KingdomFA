from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from core.models.base_model import Base
if TYPE_CHECKING:
    from core.models.feat import Feat
    from core.models.character import CharacterSkillMastery, CharacterWeaponMastery
    from core.models.character_class import CharacterClass
    from core.models.associations.worn_item_trait_association import WornItemTraitAssociation
    from core.models.associations.feat_traits_association import FeatTraitAssociation
    from core.models.associations.armor_trait_association import ArmorTraitAssociation
    from core.models.associations.weapon_trait_association import WeaponTraitAssociation
    from core.models.associations.armor_specialization_association import ArmorSpecializationAssociation
    from core.models.associations.spell_trait_association import SpellTraitAssociation
    from core.models.equipment import Worn, Armor, Weapon
    from core.models.spell import Spell


class GeneralBase(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(500), unique=True, index=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name


class GeneralDescriptionBase(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(500), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(500))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name


class DamageType(GeneralBase):
    __tablename__ = 'damage_types'

    first_type_weapons: Mapped["Weapon"] = relationship(
        "Weapon",
        foreign_keys="Weapon.damage_type_id",
        back_populates='damage_type'
    )
    second_type_weapons: Mapped["Weapon"] = relationship(
        "Weapon",
        foreign_keys="Weapon.second_damage_type_id",
        back_populates='second_damage_type'
    )


class Title(GeneralBase):
    pass


class Action(GeneralBase):
    feats: Mapped[list["Feat"]] = relationship(back_populates="action")


class Prerequisite(GeneralBase):
    feats: Mapped[list["Feat"]] = relationship(back_populates="prerequisite")


class Requirement(GeneralBase):
    feats: Mapped[list["Feat"]] = relationship(back_populates="requirement")


class Trigger(GeneralBase):
    feats: Mapped[list["Feat"]] = relationship(back_populates="trigger")


class Skill(GeneralDescriptionBase):
    character_skill_masteries: Mapped[list["CharacterSkillMastery"]] = relationship(back_populates="skill")


class WeaponMastery(GeneralDescriptionBase):
    pass


class FeatTrait(GeneralDescriptionBase):
    __tablename__ = "feat_traits"

    feats: Mapped[list["Feat"]] = relationship(
        secondary='feat_trait',
        back_populates="feat_traits",
        overlaps="feat_details"
    )
    feat_trait_details: Mapped[list["FeatTraitAssociation"]] = relationship(
        back_populates="feat_trait",
        passive_deletes=True,
        overlaps="feats"
    )


class SpellCast(GeneralBase):
    __tablename__ = 'spell_casts'

    spells: Mapped[list["Spell"]] = relationship(back_populates="spell_cast")


class SpellTradition(GeneralDescriptionBase):
    character_classes: Mapped[list["CharacterClass"]] = relationship(back_populates="spell_tradition")
    spells: Mapped[list["Spell"]] = relationship(back_populates="spell_tradition")


class SpellSchool(GeneralDescriptionBase):
    spells: Mapped[list["Spell"]] = relationship(back_populates='spell_school')


class SpellTrait(GeneralDescriptionBase):
    spells: Mapped[list["Spell"]] = relationship(
        secondary='spell_trait_association',
        back_populates='spell_traits'
    )
    spell_details: Mapped[list["SpellTraitAssociation"]] = relationship(back_populates='spell_trait')


class ArmorTrait(GeneralDescriptionBase):
    armors: Mapped[list["Armor"]] = relationship(
        secondary='armor_trait_association',
        back_populates='armor_traits'
    )
    armor_details: Mapped[list["ArmorTraitAssociation"]] = relationship(back_populates='armor_trait')


class ArmorSpecialization(GeneralDescriptionBase):
    armors: Mapped[list["Armor"]] = relationship(
        secondary='armor_specialization_association',
        back_populates='armor_specializations'
    )
    armor_details: Mapped[list["ArmorSpecializationAssociation"]] = relationship(
        back_populates='armor_specialization'
    )


class WeaponTrait(GeneralDescriptionBase):
    weapons: Mapped[list["Weapon"]] = relationship(
        secondary="weapon_trait_association",
        back_populates='weapon_traits'
    )
    weapon_details: Mapped[list["WeaponTraitAssociation"]] = relationship(
        back_populates='weapon_trait'
    )


class WeaponGroup(GeneralDescriptionBase):
    weapons: Mapped[list["Weapon"]] = relationship(back_populates='weapon_group')
    character_weapon_masteries: Mapped[list["CharacterWeaponMastery"]] = relationship(back_populates="weapon_group")


class WeaponSpecialization(GeneralDescriptionBase):
    weapons: Mapped[list["Weapon"]] = relationship(back_populates='weapon_specialization')


class WornTrait(GeneralDescriptionBase):
    worns: Mapped[list["Worn"]] = relationship(
        secondary='worn_item_trait',
        back_populates="worn_traits"
    )
    worn_details: Mapped[list["WornItemTraitAssociation"]] = relationship(
        back_populates="worn_trait",
    )
