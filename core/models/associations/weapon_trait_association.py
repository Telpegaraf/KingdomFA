from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base_model import Base

if TYPE_CHECKING:
    from core.models.equipment import Weapon
    from core.models.general import WeaponTrait


class WeaponTraitAssociation(Base):
    __tablename__ = "weapon_trait_association"
    __table_args__ = (
        UniqueConstraint(
            'weapon_id',
            'weapon_trait_id',
            name='idx_unique_weapon_trait_association'
        ),
    )

    weapon_id: Mapped[int] = mapped_column(ForeignKey("weapons.id", ondelete="CASCADE"))
    weapon_trait_id: Mapped[int] = mapped_column(ForeignKey("weapon_traits.id", ondelete="CASCADE"))

    weapon: Mapped["Weapon"] = relationship(
        back_populates="weapon_trait_details"
    )
    weapon_trait: Mapped["WeaponTrait"] = relationship(
        back_populates="weapon_details"
    )
