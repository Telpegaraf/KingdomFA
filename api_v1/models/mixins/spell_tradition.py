from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from api_v1.models.general import SpellTradition


class SpellTraditionRelationMixin:
    _spell_tradition_id_nullable: bool = False
    _spell_tradition_id_unique: bool = False
    _spell_tradition_back_populate: str | None = None

    @declared_attr
    def spell_tradition_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("spelltraditions.id"),
            unique=cls._spell_tradition_id_unique,
            nullable=cls._spell_tradition_id_nullable
        )

    @declared_attr
    def spell_tradition(cls) -> Mapped["SpellTradition"]:
        return relationship(
            "SpellTradition",
            back_populates=cls._spell_tradition_back_populate
        )
