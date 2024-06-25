from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api_v1.models.character_class import CharacterClass
    from api_v1.models.general import (
        Action,
        Trigger,
        Prerequisite,
        Requirement,
        FeatTrait
    )
    from api_v1.models.associations.feat_traits_association import FeatTraitAssociation

from api_v1.models.base_model import Base


class Feat(Base):
    character_class_id: Mapped[int] = mapped_column(
        ForeignKey("character_classes.id"),
        nullable=True
    )
    character_class: Mapped["CharacterClass"] = relationship(
        "CharacterClass",
        back_populates="feats",
    )

    feat_traits: Mapped[list["FeatTrait"]] = relationship(
        secondary="feat_trait",
        back_populates="feats"
    )
    feat_details: Mapped[list["FeatTraitAssociation"]] = relationship(
        back_populates="feat",
        passive_deletes=True
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