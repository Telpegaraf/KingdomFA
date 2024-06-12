from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING

from api_v1.models.base_model import Base
from api_v1.models.associations.god_domain_association import god_domain_association
if TYPE_CHECKING:
    from api_v1.models.god import God


class Domain(Base):
    name: Mapped[str] = mapped_column(String(50), index=True)
    gods: Mapped[list["God"]] = relationship(
        secondary=god_domain_association,
        back_populates="domains"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name
