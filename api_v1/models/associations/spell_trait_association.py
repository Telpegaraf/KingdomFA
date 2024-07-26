from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from api_v1.models.base_model import Base

if TYPE_CHECKING:
    from api_v1.models.spell import Spell
    from api_v1.models.general import SpellTrait


class SpellTraitAssociation(Base):
    __tablename__ = "spell_trait_association"
    __table_args__ = (
        UniqueConstraint(
            'spell_id',
            'spell_trait_id',
            name='idx_unique_spell_trait_association'
        ),
    )

    spell_id: Mapped[int] = mapped_column(ForeignKey("spells.id", ondelete="CASCADE"))
    spell_trait_id: Mapped[int] = mapped_column(ForeignKey("spell_traits.id", ondelete="CASCADE"))

    spell: Mapped["Spell"] = relationship(
        back_populates="spell_trait_details"
    )
    spell_trait: Mapped["SpellTrait"] = relationship(
        back_populates="spell_details"
    )
