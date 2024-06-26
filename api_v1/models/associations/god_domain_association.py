from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from api_v1.models.base_model import Base
if TYPE_CHECKING:
    from api_v1.models.domain import Domain
    from api_v1.models.god import God


class GodDomainAssociation(Base):
    __tablename__ = 'god_domain'
    __table_args__ = (
        UniqueConstraint(
            "god_id",
            "domain_id",
            name='idx_unique_god_domain'
        ),
    )

    god_id: Mapped[int] = mapped_column(ForeignKey('gods.id', ondelete="CASCADE"))
    domain_id: Mapped[int] = mapped_column(ForeignKey('domains.id', ondelete="CASCADE"))

    god: Mapped["God"] = relationship(
        back_populates='domain_details',
    )
    domain: Mapped["Domain"] = relationship(
        back_populates='god_details'
    )
