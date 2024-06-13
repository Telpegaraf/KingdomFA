from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from api_v1.models.base_model import Base


class Title(Base):
    name: Mapped[str] = mapped_column(String(50), unique=True)

    def __repr__(self):
        return self.name
