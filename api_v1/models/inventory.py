from sqlalchemy import UniqueConstraint, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from api_v1.models.base_model import Base
from api_v1.models.mixins.equipment import WeaponMixin, CurrencyMixin, ItemMixin, ArmorMixin, WornMixin
from api_v1.models.mixins.character import CharacterMixin


class CharacterCurrency(CharacterMixin, CurrencyMixin, Base):
    __tablename__ = 'character_currencies'
    __table_args__ = (
        UniqueConstraint(
            'character_id',
            'currency_id',
            name='idx_unique_character_currencies'
        ),
    )

    _character_back_populate = 'character_currencies'
    _currency_back_populate = 'character_currencies'

    quantity: Mapped[int] = mapped_column(SmallInteger, default=0)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.currency})"

    def __repr__(self):
        return self.character.__str__()


class CharacterItem(CharacterMixin, ItemMixin, Base):
    __tablename__ = 'character_items'
    __table_args__ = (
        UniqueConstraint(
            'character_id',
            'item_id',
            name='idx_unique_character_items'
        ),
    )

    _character_back_populate = 'character_items'
    _currency_back_populate = 'character_items'

    quantity: Mapped[int] = mapped_column(SmallInteger, default=0)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.item})"

    def __repr__(self):
        return self.character.__str__()


class CharacterWeapon(CharacterMixin, WeaponMixin, Base):
    __tablename__ = 'character_weapon'
    __table_args__ = (
        UniqueConstraint(
            'character_id',
            'weapon_id',
            name='idx_unique_character_weapons'
        ),
    )

    _character_back_populate = 'character_weapons'
    _currency_back_populate = 'character_weapons'

    quantity: Mapped[int] = mapped_column(SmallInteger, default=0)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.weapon})"

    def __repr__(self):
        return self.character.__str__()


class CharacterArmor(CharacterMixin, ArmorMixin, Base):
    __tablename__ = 'character_armor'
    __table_args__ = (
        UniqueConstraint(
            'character_id',
            'armor_id',
            name='idx_unique_character_armors'
        ),
    )

    _character_back_populate = 'character_armors'
    _currency_back_populate = 'character_armors'

    quantity: Mapped[int] = mapped_column(SmallInteger, default=0)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.armor})"

    def __repr__(self):
        return self.character.__str__()


class CharacterWorn(CharacterMixin, WornMixin, Base):
    __tablename__ = 'character_worn'
    __table_args__ = (
        UniqueConstraint(
            'character_id',
            'worn_id',
            name='idx_unique_character_worns'
        ),
    )

    _character_back_populate = 'character_worns'
    _currency_back_populate = 'character_worns'

    quantity: Mapped[int] = mapped_column(SmallInteger, default=0)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.worn})"

    def __repr__(self):
        return self.character.__str__()
