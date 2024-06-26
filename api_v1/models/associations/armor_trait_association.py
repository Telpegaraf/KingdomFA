from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
from api_v1.models.base_model import Base
if TYPE_CHECKING:
    from api_v1.models.general import ArmorTrait
    from api_v1.models.equipment import Armor


class ArmorTraitAssociation(Base):
    __tablename__ = 'armor_trait_association'
    __table_args__ = (
        UniqueConstraint(
            'armor_trait_id',
            'armor_id',
            name='idx_unique_armor_trait_association'
        ),
    )

    armor_trait_id: Mapped[int] = mapped_column(ForeignKey('armor_traits.id'))
    armor_id: Mapped[int] = mapped_column(ForeignKey('armors.id'))

    armor_trait: Mapped["ArmorTrait"] = relationship(
        back_populates='armor_details'
    )
    armor: Mapped["Armor"] = relationship(back_populates='armor_trait_details')
