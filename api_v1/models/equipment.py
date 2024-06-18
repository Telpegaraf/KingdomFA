from decimal import Decimal
from pydantic import Field
from sqlalchemy import String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api_v1.models.base_model import Base


class Currency(Base):
    __tablename__ = 'currencies'
    name: Mapped[str] = mapped_column(String(200), unique=True)
    price: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), default=Decimal('0.01'))
    items: Mapped[list["Item"]] = relationship(back_populates="currency")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name


class Item(Base):
    name: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[int] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), default=Decimal('0.01'))
    currency_id: Mapped[int] = mapped_column(ForeignKey('currencies.id'))
    currency: Mapped["Currency"] = relationship(back_populates='items')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name