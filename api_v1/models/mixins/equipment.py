from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from api_v1.models.equipment import Weapon, Currency, Item


class WeaponMixin:
    _weapon_id_nullable: bool = False
    _weapon_id_unique: bool = False
    _weapon_back_populate: str | None = None

    @declared_attr
    def weapon_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "weapons.id", ondelete="CASCADE"
            ),
            nullable=cls._weapon_id_nullable,
            unique=cls._weapon_id_unique
        )

    @declared_attr
    def weapon(cls) -> Mapped["Weapon"]:
        return relationship(
            back_populates=cls._weapon_back_populate
        )


class CurrencyMixin:
    _currency_id_nullable: bool = False
    _currency_id_unique: bool = False
    _currency_back_populate: str | None = None

    @declared_attr
    def currency_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "currencies.id", ondelete="CASCADE"
            ),
            nullable=cls._currency_id_nullable,
            unique=cls._currency_id_unique
        )

    @declared_attr
    def currency(cls) -> Mapped["Currency"]:
        return relationship(
            back_populates=cls._currency_back_populate
        )
