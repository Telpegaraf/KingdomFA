from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING

from api_v1.models.base_model import Base
from api_v1.models.associations.god_domain_association import god_domain_association
if TYPE_CHECKING:
    from api_v1.models.domain import Domain


class God(Base):
    name: Mapped[str] = mapped_column(String(100), index=True)
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
        secondary=god_domain_association,
        back_populates="gods"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name
