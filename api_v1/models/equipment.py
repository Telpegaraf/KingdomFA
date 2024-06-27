from decimal import Decimal
import enum
from sqlalchemy import String, Integer, ForeignKey, Numeric, Boolean, SmallInteger, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr, validates
from typing import TYPE_CHECKING

from api_v1.models.base_model import Base

if TYPE_CHECKING:
    from api_v1.models.general import(
        WornTrait,
        ArmorTrait,
        ArmorSpecialization,
        DamageType,
        WeaponTrait,
        WeaponGroup,
        WeaponSpecialization,
    )
    from api_v1.models.associations.worn_item_trait_association import WornItemTraitAssociation
    from api_v1.models.associations.armor_trait_association import ArmorTraitAssociation
    from api_v1.models.associations.weapon_trait_association import WeaponTraitAssociation
    from api_v1.models.associations.armor_specialization_association import ArmorSpecializationAssociation


class ArmorCategory(str, enum.Enum):
    UNARMED = 'Unarmed'
    LIGHT = 'Light'
    MEDIUM = 'Medium'
    HEAVY = 'Heavy'


class Dice(int, enum.Enum):
    FOUR = 4
    SIX = 6
    EIGHT = 8
    TEN = 10
    TWELVE = 12
    TWENTY = 20


class Currency(Base):
    __tablename__ = 'currencies'

    name: Mapped[str] = mapped_column(String(200), unique=True)
    price: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), default=Decimal('0.01'))
    worns: Mapped[list["Worn"]] = relationship(back_populates="currency")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name


class Item(Base):
    __abstract__ = True

    _item_back_populate: str | None = None

    name: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[int] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), default=Decimal('0.01'))

    @declared_attr
    def currency_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('currencies.id'))

    @declared_attr
    def currency(cls) -> Mapped["Currency"]:
        return relationship(back_populates=cls._item_back_populate)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name


class Slot(Base):
    slot: Mapped[str] = mapped_column(String(100), unique=True)
    limit: Mapped[bool] = mapped_column(Boolean)
    worn_items: Mapped[list["Worn"]] = relationship(back_populates='slot')


class Worn(Item):
    _item_back_populate = 'worns'
    slot_id: Mapped[int] = mapped_column(ForeignKey('slots.id'))
    slot: Mapped["Slot"] = relationship(back_populates='worn_items')

    level: Mapped[int] = mapped_column(SmallInteger, default=0)
    activate: Mapped[str] = mapped_column(String)
    effect: Mapped[str] = mapped_column(String)
    worn_traits: Mapped[list["WornTrait"]] = relationship(
        secondary='worn_item_trait',
        back_populates="worns"
    )

    worn_trait_details: Mapped[list["WornItemTraitAssociation"]] = relationship(
        "WornItemTraitAssociation",
        back_populates="worn",
    )


class ArmorGroup(Base):
    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(500))
    hardness:Mapped[int] = mapped_column(SmallInteger, default=1)
    health: Mapped[int] = mapped_column(SmallInteger)
    broken_threshold: Mapped[int] = mapped_column(SmallInteger)

    armors: Mapped[list["Armor"]] = relationship(back_populates='armor_group')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name


class Armor(Item):
    armor_group_id: Mapped[int] = mapped_column(ForeignKey("armor_groups.id"))
    armor_group: Mapped["ArmorGroup"] = relationship(back_populates='armors')

    category: Mapped[ArmorCategory] = mapped_column(Enum(ArmorCategory), default=ArmorCategory.UNARMED)
    ac_bonus: Mapped[int] = mapped_column(SmallInteger, default=0)
    dexterity_modifier_cap: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    check_penalty: Mapped[bool] = mapped_column(Boolean)
    speed_penalty: Mapped[bool] = mapped_column(Boolean)
    strength: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    level: Mapped[int] = mapped_column(SmallInteger, default=0)

    armor_traits: Mapped[list["ArmorTrait"]] = relationship(
        secondary='armor_trait_association',
        back_populates='armors'
    )
    armor_trait_details: Mapped[list["ArmorTraitAssociation"]] = relationship(
        back_populates='armor',
    )

    armor_specializations: Mapped[list["ArmorSpecialization"]] = relationship(
        secondary='armor_specialization_association',
        back_populates='armors'
    )
    armor_specialization_details: Mapped[list["ArmorSpecializationAssociation"]] = relationship(
        back_populates='armor',
    )


class Weapon(Item):
    damage_type_id: Mapped[int] = mapped_column(ForeignKey("damage_types.id", ondelete="CASCADE"))
    damage_type: Mapped["DamageType"] = relationship(
        "DamageType",
        foreign_keys=[damage_type_id],
        back_populates='first_type_weapons'
    )
    second_damage_type_id: Mapped[int] = mapped_column(ForeignKey(
        "damage_types.id",
        ondelete="CASCADE"),
        nullable=True
    )
    second_damage_type: Mapped["DamageType"] = relationship(
        "DamageType",
        foreign_keys=[second_damage_type_id],
        back_populates='second_type_weapons'
    )
    weapon_group_id: Mapped[int] = mapped_column(ForeignKey('weapon_groups.id'), nullable=True)
    weapon_group: Mapped["WeaponGroup"] = relationship(back_populates='weapons')
    weapon_specialization_id: Mapped[int] = mapped_column(ForeignKey('weapon_specializations.id'), nullable=True)
    weapon_specialization: Mapped["WeaponSpecialization"] = relationship(back_populates='weapons')

    dice: Mapped[Dice] = mapped_column(Enum(Dice), default=Dice.FOUR)
    dice_count: Mapped[int] = mapped_column(SmallInteger, default=1)
    bonus_damage: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    second_dice: Mapped[Dice] = mapped_column(Enum(Dice), nullable=True)
    second_dice_count: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    second_bonus_damage: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    range: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    reload: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    two_hands: Mapped[bool] = mapped_column(Boolean, default=True)
    level: Mapped[int] = mapped_column(SmallInteger, default=0)

    weapon_traits: Mapped[list["WeaponTrait"]] = relationship(
        secondary="weapon_trait_association",
        back_populates='weapons'
    )
    weapon_trait_details: Mapped[list["WeaponTraitAssociation"]] = relationship(
        back_populates='weapon'
    )
