from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from api_v1.models.base_model import Base
if TYPE_CHECKING:
    from api_v1.models.general import FeatTrait
    from api_v1.models.feat_class import Feat


class FeatTraitAssociation(Base):
    __tablename__ = 'feat_trait'
    __table_args__ = (
        UniqueConstraint(
            "feat_id",
            "trait_id",
            name='idx_unique_feat_trait'
        ),
    )

    feat_id: Mapped[int] = mapped_column(ForeignKey('feats.id'))
    trait_id: Mapped[int] = mapped_column(ForeignKey('feat_traits.id'))

    feat: Mapped["Feat"] = relationship(
        back_populates='feat_details',
    )
    feat_trait: Mapped["FeatTrait"] = relationship(
        back_populates='feat_trait_details'
    )
