from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base_model import Base
if TYPE_CHECKING:
    from core.models.general import FeatTrait
    from core.models.feat import Feat


class FeatTraitAssociation(Base):
    __tablename__ = 'feat_trait'
    __table_args__ = (
        UniqueConstraint(
            "feat_id",
            "trait_id",
            name='idx_unique_feat_trait'
        ),
    )

    feat_id: Mapped[int] = mapped_column(ForeignKey('feats.id', ondelete="CASCADE"))
    trait_id: Mapped[int] = mapped_column(ForeignKey('feat_traits.id', ondelete="CASCADE"))

    feat: Mapped["Feat"] = relationship(
        back_populates='feat_details',
        overlaps="feat_traits"
    )
    feat_trait: Mapped["FeatTrait"] = relationship(
        back_populates='feat_trait_details',
        overlaps="feats"
    )
