from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from typing import TYPE_CHECKING

from api_v1.models import Base
if TYPE_CHECKING:
    from api_v1.models.feat import Feat
    from api_v1.models.character_class import CharacterClass
    from api_v1.models.associations.worn_item_trait_association import WornItemTraitAssociation
    from api_v1.models.associations.feat_traits_association import FeatTraitAssociation
    from api_v1.models.associations.armor_trait_association import ArmorTraitAssociation
    from api_v1.models.associations.weapon_trait_association import WeaponTraitAssociation
    from api_v1.models.associations.armor_specialization_association import ArmorSpecializationAssociation
    from api_v1.models.equipment import Worn, Armor, Weapon
    from api_v1.models.spell import Spell


class GeneralBase(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(500), unique=True, index=True)

    @declared_attr
    def __str__(cls):
        def __str__(self):
            return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

        return __str__

    @declared_attr
    def __repr__(cls):
        def __repr__(self):
            return self.name

        return __repr__


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


class Skills(GeneralDescriptionBase):
    pass


class WeaponMastery(GeneralDescriptionBase):
    pass


class FeatTrait(GeneralDescriptionBase):
    __tablename__ = "feat_traits"

    feats: Mapped[list["Feat"]] = relationship(
        secondary='feat_trait',
        back_populates="feat_traits"
    )
    feat_trait_details: Mapped[list["FeatTraitAssociation"]] = relationship(
        back_populates="feat_trait",
        passive_deletes=True
    )


class SpellCast(GeneralBase):
    __tablename__ = 'spell_casts'

    spells: Mapped[list["Spell"]] = relationship(back_populates="spell_cast")


class SpellTradition(GeneralDescriptionBase):
    character_classes: Mapped[list["CharacterClass"]] = relationship(back_populates="spell_tradition")
    spells: Mapped[list["Spell"]] = relationship(back_populates="spells")


class SpellSchool(GeneralDescriptionBase):
    spells: Mapped[list["Spell"]] = relationship(back_populates='spell_school')


class SpellTrait(GeneralDescriptionBase):
    spells: Mapped[list["Spell"]] = relationship(back_populates='spell_trait')


class SpellComponent(GeneralDescriptionBase):
    spells: Mapped[list["Spell"]] = relationship(back_populates='spell_component')


class ArmorTrait(GeneralDescriptionBase):
    armors: Mapped[list["Armor"]] = relationship(
        secondary='armor_trait_association',
        back_populates='armor_traits'
    )
    armor_trait_details: Mapped[list["ArmorTraitAssociation"]] = relationship(back_populates='armor_trait')


class ArmorSpecialization(GeneralDescriptionBase):
    armors: Mapped[list["Armor"]] = relationship(
        secondary='armor_specialization_association',
        back_populates='armor_specialization'
    )
    armor_specialization_details: Mapped[list["ArmorSpecializationAssociation"]] = relationship(
        back_populates='armor_specialization'
    )


class WeaponTrait(GeneralDescriptionBase):
    weapons: Mapped[list["Weapon"]] = relationship(
        back_populates='weapon_traits'
    )
    weapon_detail: Mapped[list["WeaponTraitAssociation"]] = relationship(
        back_populates='weapon_trait'
    )


class WeaponGroup(GeneralDescriptionBase):
    weapons: Mapped[list["Weapon"]] = relationship(back_populates='weapon_group')


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
