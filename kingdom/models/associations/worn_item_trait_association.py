from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from kingdom.models.base_model import Base
if TYPE_CHECKING:
    from kingdom.models.general import WornTrait
    from kingdom.models.equipment import Worn


class WornItemTraitAssociation(Base):
    __tablename__ = 'worn_item_trait'
    __table_args__ = (
        UniqueConstraint(
            "worn_id",
            "worn_trait_id",
            name='idx_unique_worn_item_trait'
        ),
    )

    worn_id: Mapped[int] = mapped_column(ForeignKey('worns.id', ondelete="CASCADE"))
    worn_trait_id: Mapped[int] = mapped_column(ForeignKey('worn_traits.id', ondelete="CASCADE"))

    worn: Mapped["Worn"] = relationship(
        back_populates='worn_trait_details',
    )
    worn_trait: Mapped["WornTrait"] = relationship(
        back_populates='worn_details'
    )
