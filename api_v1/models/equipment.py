from decimal import Decimal
from pydantic import Field
from sqlalchemy import String, Integer, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from typing import TYPE_CHECKING

from api_v1.models.base_model import Base

if TYPE_CHECKING:
    from api_v1.models.general import WornTrait
    from api_v1.models.associations.worn_item_trait_association import WornItemTraitAssociation


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
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[int] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), default=Decimal('0.01'))

    @declared_attr
    def currency_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('currencies.id'))

    @declared_attr
    def currency(cls) -> Mapped["Currency"]:
        return relationship(back_populates='items')

    @declared_attr.directive
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    @declared_attr.directive
    def __repr__(self):
        return self.name


class Slot(Base):
    slot: Mapped[str] = mapped_column(String(100), unique=True)
    limit: Mapped[bool] = mapped_column(Boolean)
    worn_items: Mapped[list["Worn"]] = relationship(back_populates='slot')


class Worn(Item):
    slot_id: Mapped[int] = mapped_column(ForeignKey('slots.id'))
    slot: Mapped["Slot"] = relationship(back_populates='worn_items')
    level: Mapped[int] = mapped_column(Integer)
    activate: Mapped[str] = mapped_column(String)
    effect: Mapped[str] = mapped_column(String)
    worn_traits: Mapped[list["WornTrait"]] = relationship(
        secondary='worn_item_trait',
        back_populates="worns"
    )

    worn_trait_details: Mapped[list["WornItemTraitAssociation"]] = relationship(
        "WornItemTraitAssociation",
        back_populates="worn",
        passive_deletes=True
    )
