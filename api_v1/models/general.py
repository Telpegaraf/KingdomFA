from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from typing import TYPE_CHECKING

from api_v1.models import Base
if TYPE_CHECKING:
    from api_v1.models.feat import Feat
    from api_v1.models.character_class import CharacterClass
    from api_v1.models.associations.worn_item_trait_association import WornItemTraitAssociation
    from api_v1.models.associations.feat_traits_association import FeatTraitAssociation
    from api_v1.models.equipment import Worn


class GeneralBase(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(500), unique=True, index=True)

    @declared_attr.directive
    def __str__(self):
        return f"{self.__class__.name}(id={self.id}, name={self.name!r})"

    @declared_attr.directive
    def __repr__(self):
        return self.name


class GeneralDescriptionBase(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(500), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(500))


class DamageType(GeneralBase):
    pass


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


class SpellCast(GeneralBase):
    pass


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


class SpellTradition(GeneralDescriptionBase):
    character_classes: Mapped[list["CharacterClass"]] = relationship(back_populates="spell_tradition")


class SpellSchool(GeneralDescriptionBase):
    pass


class SpellTrait(GeneralDescriptionBase):
    pass


class SpellComponent(GeneralDescriptionBase):
    pass


class ArmorTrait(GeneralDescriptionBase):
    pass


class ArmorSpecialization(GeneralDescriptionBase):
    pass


class WeaponTrait(GeneralDescriptionBase):
    pass


class WeaponGroup(GeneralDescriptionBase):
    pass


class WeaponSpecialization(GeneralDescriptionBase):
    pass


class WornTrait(GeneralDescriptionBase):
    __tablename__ = 'worn_traits'

    worns: Mapped[list["Worn"]] = relationship(
        secondary='worn_item_trait',
        back_populates="worn_traits"
    )
    worn_details: Mapped[list["WornItemTraitAssociation"]] = relationship(
        back_populates="worn_trait",
    )
