from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from api_v1.general.models import Race



class RaceRelationMixin:
    _race_id_nullable: bool = False
    _race_id_unique: bool = False
    _race_back_populate: str | None = None

    race_id: Mapped[int] = mapped_column(ForeignKey("race_table.id"))

    @declared_attr
    def race_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("races.id"),
            unique=cls._race_id_unique,
            nullable=cls._race_id_nullable
        )

    @declared_attr
    def race(cls) -> Mapped["Race"]:
        return relationship(
            "Race",
            back_populates=cls._race_back_populate
        )
