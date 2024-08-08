from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from kingdom.models.feat import Feat


class FeatMixin:
    _feat_id_nullable: bool = False
    _feat_id_unique: bool = False
    _feat_back_populate: str | None = None

    @declared_attr
    def feat_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "feats.id", ondelete="CASCADE"
            ),
            nullable=cls._feat_id_nullable,
            unique=cls._feat_id_unique
        )

    @declared_attr
    def feat(cls) -> Mapped["Feat"]:
        return relationship(
            back_populates=cls._feat_back_populate
        )
