from pydantic import EmailStr
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api_v1.models.base_model import Base
if TYPE_CHECKING:
    from api_v1.models.character import Character


class User(Base):
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(120))
    email: Mapped[Optional[EmailStr]] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, server_default='f', default=False)
    characters: Mapped[List["Character"]] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.username!r}"

    def __repr__(self):
        return self.username
