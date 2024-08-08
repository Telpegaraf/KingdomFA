from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from kingdom.models.character_class import CharacterClass


class CharacterClassMixin:
    _character_class_id_nullable: bool = False
    _character_class_id_unique: bool = False
    _character_class_back_populate: str | None = None

    @declared_attr
    def character_class_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("character_classes.id", ondelete="CASCADE"),
            nullable=cls._character_class_id_nullable,
            unique=cls._character_class_id_unique
        )

    @declared_attr
    def character_class(cls) -> Mapped["CharacterClass"]:
        return relationship(
            back_populates=cls._character_class_back_populate
        )
