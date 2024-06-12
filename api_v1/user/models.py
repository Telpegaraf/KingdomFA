from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models import Base
if TYPE_CHECKING:
    from api_v1.character.models import Character


class User(Base):
    username: Mapped[str] = mapped_column(String(100), unique=True)
    characters: Mapped[list["Character"]] = relationship(back_populates="user")
