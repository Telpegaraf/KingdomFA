from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING

from api_v1.models.base_model import Base

if TYPE_CHECKING:
    from api_v1.models.domain import Domain
    from api_v1.models.associations.god_domain_association import GodDomainAssociation
    from api_v1.models.character import Character


class God(Base):
    characters: Mapped[list["Character"]] = relationship(back_populates="domain")

    name: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    alias: Mapped[str] = mapped_column(String(100))
    edict: Mapped[str] = mapped_column(String(300))
    anathema: Mapped[str] = mapped_column(String(300))
    areas_of_interest: Mapped[str] = mapped_column(String(300))
    temples: Mapped[str] = mapped_column(String(300))
    worship: Mapped[str] = mapped_column(String(300))
    sacred_animal: Mapped[str] = mapped_column(String(300))
    sacred_color: Mapped[str] = mapped_column(String(300))
    chosen_weapon: Mapped[str] = mapped_column(String(300))
    taro: Mapped[str] = mapped_column(String(300))
    alignment: Mapped[str] = mapped_column(String(300))
    domains: Mapped[list["Domain"]] = relationship(
        secondary='god_domain',
        back_populates="gods"
    )

    domain_details: Mapped[list["GodDomainAssociation"]] = relationship(
        "GodDomainAssociation",
        back_populates="god",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name
