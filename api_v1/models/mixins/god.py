from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from api_v1.models.god import God
    from api_v1.models.domain import Domain


class GodMixin:
    _god_id_nullable: bool = False
    _god_id_unique: bool = False
    _god_back_populate: str | None = None

    @declared_attr
    def god_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "gods.id", ondelete="CASCADE"
            ),
            nullable=cls._god_id_nullable,
            unique=cls._god_id_unique
        )

    @declared_attr
    def god(cls) -> Mapped["God"]:
        return relationship(
            back_populates=cls._god_back_populate
        )


class DomainMixin:
    _domain_id_nullable: bool = False
    _domain_id_unique: bool = False
    _domain_back_populate: str | None = None

    @declared_attr
    def domain_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "domains.id", ondelete="CASCADE",
            ),
            nullable=cls._domain_id_nullable,
            unique=cls._domain_id_unique
        )

    @declared_attr
    def domain(cls) -> Mapped["Domain"]:
        return relationship(
            back_populates=cls._domain_back_populate
        )
