from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from kingdom.models.general import (
        Action,
        Trigger,
        Prerequisite,
        Requirement,
        FeatTrait
    )
    from kingdom.models.associations.feat_traits_association import FeatTraitAssociation
    from kingdom.models.character_class import Background, Feature

from kingdom.models.base_model import Base
from kingdom.models.mixins.character_class import CharacterClassMixin


class Feat(CharacterClassMixin, Base):
    _character_class_back_populate = "feats"
    _character_class_id_nullable = True

    backgrounds: Mapped[list["Background"]] = relationship(back_populates="feat")
    features: Mapped[list["Feature"]] = relationship(back_populates="feat")

    feat_traits: Mapped[list["FeatTrait"]] = relationship(
        secondary="feat_trait",
        back_populates="feats",
        overlaps="feat_trait_details"
    )
    feat_details: Mapped[list["FeatTraitAssociation"]] = relationship(
        back_populates="feat",
        passive_deletes=True,
        overlaps="feat_trait"
    )

    action_id: Mapped[int] = mapped_column(ForeignKey("actions.id"))
    action: Mapped["Action"] = relationship(back_populates="feats")
    trigger_id: Mapped[int] = mapped_column(ForeignKey("triggers.id"))
    trigger: Mapped["Trigger"] = relationship(back_populates="feats")
    prerequisite_id: Mapped[int] = mapped_column(ForeignKey("prerequisites.id"))
    prerequisite: Mapped["Prerequisite"] = relationship(back_populates="feats")
    requirement_id: Mapped[int] = mapped_column(ForeignKey("requirements.id"))
    requirement: Mapped["Requirement"] = relationship(back_populates='feats')

    name: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[str] = mapped_column(String(500))
    level: Mapped[int] = mapped_column(Integer, default=0)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name
