from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from kingdom.models.general import(
        SpellTradition,
        SpellSchool,
        SpellCast,
        SpellTrait
    )


class SpellTraditionMixin:
    _spell_tradition_id_nullable: bool = False
    _spell_tradition_id_unique: bool = False
    _spell_tradition_back_populate: str | None = None

    @declared_attr
    def spell_tradition_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("spell_traditions.id", ondelete="CASCADE"),
            unique=cls._spell_tradition_id_unique,
            nullable=cls._spell_tradition_id_nullable

        )

    @declared_attr
    def spell_tradition(cls) -> Mapped["SpellTradition"]:
        return relationship(
            back_populates=cls._spell_tradition_back_populate
        )


class SpellSchoolMixin:
    _spell_school_id_nullable: bool = False
    _spell_school_id_unique: bool = False
    _spell_school_back_populate: str | None = None

    @declared_attr
    def spell_school_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "spell_schools.id", ondelete="CASCADE"
            ),
            nullable=cls._spell_school_id_nullable,
            unique=cls._spell_school_id_unique
        )

    @declared_attr
    def spell_school(cls) -> Mapped["SpellSchool"]:
        return relationship(
            back_populates=cls._spell_school_back_populate
        )


class SpellCastMixin:
    _spell_cast_id_nullable: bool = False
    _spell_cast_id_unique: bool = False
    _spell_cast_back_populate: str | None = None

    @declared_attr
    def spell_cast_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "spell_casts.id", ondelete="CASCADE"
            ),
            nullable=cls._spell_cast_id_nullable,
            unique=cls._spell_cast_id_unique
        )

    @declared_attr
    def spell_cast(cls) -> Mapped["SpellCast"]:
        return relationship(
            back_populates=cls._spell_cast_back_populate
        )


class SpellTraitMixin:
    _spell_trait_id_nullable: bool = False
    _spell_trait_id_unique: bool = False
    _spell_trait_back_populate: str | None = None

    @declared_attr
    def spell_trait_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "spell_traits.id", ondelete="CASCADE"
            ),
            nullable=cls._spell_trait_id_nullable,
            unique=cls._spell_trait_id_unique
        )

    @declared_attr
    def spell_trait(cls) -> Mapped["SpellTrait"]:
        return relationship(
            back_populates=cls._spell_trait_back_populate
        )
