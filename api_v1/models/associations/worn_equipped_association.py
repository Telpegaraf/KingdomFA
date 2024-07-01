from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, mapped_column, Mapped
from api_v1.models.base_model import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api_v1.models.inventory import EquippedItems, CharacterWorn


class WornEquippedAssociation(Base):
    __tablename__ = 'worn_equipped_association'
    __table_args__ = (
        UniqueConstraint(
            'inventory_worn_id',
            'equipped_worn_id',
            name='idx_unique_worn_equipped'
        ),
    )

    inventory_worn_id: Mapped[int] = mapped_column(ForeignKey("character_worns.id", ondelete="CASCADE"))
    equipped_worn_id: Mapped[int] = mapped_column(ForeignKey("equipped_items.id", ondelete="CASCADE"))

    inventory_worn: Mapped["CharacterWorn"] = relationship(back_populates="equipped_worn_details")
    equipped_worn: Mapped["EquippedItems"] = relationship(back_populates="inventory_worn_details")
