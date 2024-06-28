from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from api_v1.models.character import Character


class CharacterMixin:
    _character_id_nullable: bool = False
    _character_id_unique: bool = False
    _character_back_populate: str | None = None

    @declared_attr
    def character_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "characters.id", ondelete="CASCADE"
            ),
            nullable=cls._character_id_nullable,
            unique=cls._character_id_unique
        )

    @declared_attr
    def character(cls) -> Mapped["Character"]:
        return relationship(
            back_populates=cls._character_back_populate
        )
