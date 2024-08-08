from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
from kingdom.models.base_model import Base
if TYPE_CHECKING:
    from kingdom.models.general import ArmorTrait
    from kingdom.models.equipment import Armor


class ArmorTraitAssociation(Base):
    __tablename__ = 'armor_trait_association'
    __table_args__ = (
        UniqueConstraint(
            'armor_trait_id',
            'armor_id',
            name='idx_unique_armor_trait_association'
        ),
    )

    armor_trait_id: Mapped[int] = mapped_column(ForeignKey('armor_traits.id', ondelete="CASCADE"))
    armor_id: Mapped[int] = mapped_column(ForeignKey('armors.id', ondelete="CASCADE"))

    armor_trait: Mapped["ArmorTrait"] = relationship(
        back_populates='armor_details'
    )
    armor: Mapped["Armor"] = relationship(back_populates='armor_trait_details')
