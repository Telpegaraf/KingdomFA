from sqlalchemy import UniqueConstraint, SmallInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from api_v1.models.base_model import Base
from api_v1.models.mixins.equipment import WeaponMixin, CurrencyMixin, ItemMixin, ArmorMixin, WornMixin
from api_v1.models.mixins.character import CharacterMixin
if TYPE_CHECKING:
    from api_v1.models.associations.worn_equipped_association import WornEquippedAssociation


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
    __tablename__ = 'character_weapons'
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

    first_equipped_weapon: Mapped["EquippedItems"] = relationship(
        foreign_keys="EquippedItems.first_weapon_id",
        back_populates='first_weapon'
    )
    second_equipped_weapon: Mapped["EquippedItems"] = relationship(
        foreign_keys="EquippedItems.second_weapon_id",
        back_populates='second_weapon'
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.weapon})"

    def __repr__(self):
        return self.character.__str__()


class CharacterArmor(CharacterMixin, ArmorMixin, Base):
    __tablename__ = 'character_armors'
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
    equipped_armor: Mapped["EquippedItems"] = relationship(back_populates='armor')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.armor})"

    def __repr__(self):
        return self.character.__str__()


class CharacterWorn(CharacterMixin, WornMixin, Base):
    __tablename__ = 'character_worns'
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

    equipped_worns: Mapped[list["EquippedItems"]] = relationship(
        secondary='worn_equipped_association',
        back_populates='character_worns'
    )
    equipped_worn_details: Mapped[list["WornEquippedAssociation"]] = relationship(
        back_populates='character_worn'
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}," \
               f" name={self.character.__str__()!r}'s {self.worn})"

    def __repr__(self):
        return self.character.__str__()


class EquippedItems(CharacterMixin, Base):
    _character_back_populate = 'equipped_items'

    first_weapon_id: Mapped[int] = mapped_column(
        ForeignKey(
            "character_weapons.id", ondelete="CASCADE"
        ),
        nullable=True
    )
    first_weapon: Mapped["CharacterWeapon"] = relationship(
        foreign_keys=[first_weapon_id],
        back_populates='first_equipped_weapon'
    )
    second_weapon_id: Mapped[int] = mapped_column(
        ForeignKey(
            "character_weapons.id", ondelete="CASCADE"
        ),
        nullable=True
    )
    second_weapon: Mapped["CharacterWeapon"] = relationship(
        foreign_keys=[second_weapon_id],
        back_populates='second_equipped_weapon'
    )
    armor_id: Mapped[int] = mapped_column(
        ForeignKey(
            "character_armors.id", ondelete="CASCADE"
        ),
        nullable=True
    )
    armor: Mapped["CharacterArmor"] = relationship(back_populates='equipped_armor')

    character_worns: Mapped[list["CharacterWorn"]] = relationship(
        secondary='worn_equipped_association',
        back_populates='equipped_worns'
    )
    inventory_worn_details: Mapped[list["WornEquippedAssociation"]] = relationship(
        back_populates='equipped_worn'
    )
