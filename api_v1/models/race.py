from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from api_v1.models.base_model import Base
if TYPE_CHECKING:
    from api_v1.models.character import Character


class Race(Base):
    name: Mapped[str] = mapped_column(String(50), unique=True)
    characters: Mapped[list["Character"]] = relationship(back_populates="race")

    def __repr__(self):
        return self.name
