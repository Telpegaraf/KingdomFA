from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from kingdom.models.base_model import Base
if TYPE_CHECKING:
    from kingdom.models.character import Character


class Race(Base):
    # field
    name: Mapped[str] = mapped_column(String(50), unique=True)
    # relations
    characters: Mapped[list["Character"]] = relationship(back_populates="race")

    def __repr__(self):
        return self.name
