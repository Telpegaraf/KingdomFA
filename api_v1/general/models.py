from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from core.models import Base


class Race(Base):
    name: Mapped[str] = mapped_column(String(50), unique=True)

    def __repr__(self):
        return self.name
