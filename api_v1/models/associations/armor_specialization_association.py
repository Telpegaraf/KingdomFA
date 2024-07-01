from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from api_v1.models.general import ArmorSpecialization
    from api_v1.models.equipment import Armor

from api_v1.models.base_model import Base


class ArmorSpecializationAssociation(Base):
    __tablename__ = 'armor_specialization_association'
    __table_args__ = (
        UniqueConstraint(
            'armor_id',
            'armor_specialization_id',
            name='idx_unique_armor_specialization_association'
        ),
    )

    armor_id: Mapped[int] = mapped_column(ForeignKey('armors.id'))
    armor_specialization_id: Mapped[int] = mapped_column(ForeignKey('armor_specializations.id'))

    armor: Mapped["Armor"] = relationship(back_populates='armor_specialization_details')
    armor_specialization: Mapped["ArmorSpecialization"] = relationship(
        back_populates='armor_details'
    )
