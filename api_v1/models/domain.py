from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING

from api_v1.models.base_model import Base

if TYPE_CHECKING:
    from api_v1.models.god import God
    from api_v1.models.associations.god_domain_association import GodDomainAssociation


class Domain(Base):
    name: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    gods: Mapped[list["God"]] = relationship(
        secondary='god_domain',
        back_populates="domains"
    )

    god_details: Mapped[list["GodDomainAssociation"]] = relationship(
        "GodDomainAssociation",
        back_populates="domain",
        passive_deletes=True
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name
