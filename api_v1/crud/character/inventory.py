from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api_v1.utils.model_result import get_model_result
from api_v1.schemas.character.inventory import (
    CharacterArmorCreateUpdate,
    CharacterCurrencyCreateUpdate,
    CharacterItemCreateUpdate,
    CharacterWeaponCreateUpdate,
    CharacterWornCreateUpdate
)
from core.models.inventory import (
    CharacterWorn,
    CharacterArmor,
    CharacterItem,
    CharacterWeapon,
    CharacterCurrency
)
from core.models.equipment import Currency, Item, Armor, Weapon, Worn
from core.models.character import Character


async def character_currency_list(session: AsyncSession):
    stmt = select(CharacterCurrency).options(
        selectinload(CharacterCurrency.currency),
        selectinload(CharacterCurrency.character)
    ).order_by(CharacterCurrency.id)
    result: Result = await session.execute(stmt)
    currencies = result.scalars().all()
    return list(currencies)


async def character_currency_detail(session: AsyncSession, character_currency_id: int) -> CharacterCurrency | None:
    return await session.scalar(
        select(CharacterCurrency)
        .where(CharacterCurrency.id == character_currency_id)
        .options(selectinload(CharacterCurrency.currency),
                 selectinload(CharacterCurrency.character))
    )


async def character_currency_create(
        session: AsyncSession,
        character_currency_in: CharacterCurrencyCreateUpdate
) -> CharacterCurrency:
    currency = await get_model_result(model=Currency, object_id=character_currency_in.currency_id, session=session)
    character = await get_model_result(model=Character, object_id=character_currency_in.character_id, session=session)
    character_currency = CharacterCurrency(
        currency=currency,
        character=character,
        quantity=character_currency_in.quantity
    )
    session.add(character_currency)
    await session.commit()
    await session.refresh(character_currency)
    return await character_currency_detail(session=session, character_currency_id=character_currency.id)


async def character_currency_update(
        session: AsyncSession,
        character_currency_update: CharacterCurrencyCreateUpdate,
        character_currency: CharacterCurrency
):
    currency = await get_model_result(model=Currency, object_id=character_currency_update.currency_id, session=session)
    setattr(character_currency, 'quantity', character_currency_update.quantity)
    character_currency.currency = currency
    await session.commit()
    await session.refresh(character_currency)
    return character_currency


async def character_currency_delete(
        session: AsyncSession,
        character_currency: CharacterCurrency
):
    await session.delete(character_currency)
    await session.commit()


async def character_item_list(session: AsyncSession):
    stmt = select(CharacterItem).options(
        selectinload(CharacterItem.character),
        selectinload(CharacterItem.item).joinedload(Item.currency)
    ).order_by(CharacterItem.id)
    result: Result = await session.execute(stmt)
    items = result.scalars().all()
    return list(items)


async def character_item_detail(session: AsyncSession, character_item_id: int) -> CharacterItem | None:
    return await session.scalar(
        select(CharacterItem)
        .where(CharacterItem.id == character_item_id)
        .options(selectinload(CharacterItem.character),
                 selectinload(CharacterItem.item).joinedload(Item.currency))
    )


async def character_item_create(
        session: AsyncSession,
        character_item_in: CharacterItemCreateUpdate
) -> CharacterItem:
    character = await get_model_result(model=Character, object_id=character_item_in.character_id, session=session)
    item = await get_model_result(model=Item, object_id=character_item_in.item_id, session=session)
    character_item = CharacterItem(
        item=item,
        character=character,
        quantity=character_item_in.quantity
    )
    session.add(character_item)
    await session.commit()
    await session.refresh(character_item)
    return await character_item_detail(session=session, character_item_id=character_item.id)


async def character_item_update(
        session: AsyncSession,
        character_item_update: CharacterItemCreateUpdate,
        character_item: CharacterItem
):
    item = await get_model_result(model=Item, object_id=character_item_update.item_id, session=session)
    setattr(character_item, 'quantity', character_item_update.quantity)
    character_item.item = item
    await session.commit()
    await session.refresh(character_item)
    return character_item


async def character_item_delete(
        session: AsyncSession,
        character_item: CharacterItem
):
    await session.delete(character_item)
    await session.commit()


async def character_armor_list(session: AsyncSession):
    stmt = select(CharacterArmor).options(
        selectinload(CharacterArmor.character),
        selectinload(CharacterArmor.armor).selectinload(Armor.currency),
        selectinload(CharacterArmor.armor).selectinload(Armor.armor_specializations),
        selectinload(CharacterArmor.armor).selectinload(Armor.armor_traits),
        selectinload(CharacterArmor.armor).selectinload(Armor.armor_group)
    ).order_by(CharacterArmor.id)
    result: Result = await session.execute(stmt)
    armors = result.scalars().all()
    return list(armors)


async def character_armor_detail(session: AsyncSession, character_armor_id: int) -> CharacterArmor | None:
    return await session.scalar(
        select(CharacterArmor)
        .where(CharacterArmor.id == character_armor_id)
        .options(
            selectinload(CharacterArmor.character),
            selectinload(CharacterArmor.armor).selectinload(Armor.currency),
            selectinload(CharacterArmor.armor).selectinload(Armor.armor_specializations),
            selectinload(CharacterArmor.armor).selectinload(Armor.armor_traits),
            selectinload(CharacterArmor.armor).selectinload(Armor.armor_group)
        )
    )


async def character_armor_create(
        session: AsyncSession,
        character_armor_in: CharacterArmorCreateUpdate
) -> CharacterArmor:
    character = await get_model_result(model=Character, object_id=character_armor_in.character_id, session=session)
    armor = await get_model_result(model=Armor, object_id=character_armor_in.armor_id, session=session)
    character_armor = CharacterArmor(
        armor=armor,
        character=character,
        quantity=character_armor_in.quantity
    )
    session.add(character_armor)
    await session.commit()
    await session.refresh(character_armor)
    return await character_armor_detail(session=session, character_armor_id=character_armor.id)


async def character_armor_update(
        session: AsyncSession,
        character_armor_update: CharacterArmorCreateUpdate,
        character_armor: CharacterArmor
):
    armor = await get_model_result(model=Armor, object_id=character_armor_update.armor_id, session=session)
    setattr(character_armor, 'quantity', character_armor_update.quantity)
    character_armor.armor = armor
    await session.commit()
    await session.refresh(character_armor)
    return character_armor


async def character_armor_delete(
        session: AsyncSession,
        character_armor: CharacterArmor
):
    await session.delete(character_armor)
    await session.commit()


async def character_weapon_list(session: AsyncSession):
    stmt = select(CharacterWeapon).options(
        selectinload(CharacterWeapon.character),
        selectinload(CharacterWeapon.weapon).selectinload(Weapon.weapon_group),
        selectinload(CharacterWeapon.weapon).selectinload(Weapon.weapon_specialization),
        selectinload(CharacterWeapon.weapon).selectinload(Weapon.weapon_traits),
        selectinload(CharacterWeapon.weapon).selectinload(Weapon.currency),
        selectinload(CharacterWeapon.weapon).selectinload(Weapon.damage_type),
        selectinload(CharacterWeapon.weapon).selectinload(Weapon.second_damage_type)
    ).order_by(CharacterWeapon.id)
    result: Result = await session.execute(stmt)
    weapons = result.scalars().all()
    return list(weapons)


async def character_weapon_detail(session: AsyncSession, character_weapon_id: int) -> CharacterWeapon | None:
    return await session.scalar(
        select(CharacterWeapon)
        .where(CharacterWeapon.id == character_weapon_id)
        .options(selectinload(CharacterWeapon.character),
                 selectinload(CharacterWeapon.weapon).selectinload(Weapon.weapon_group),
                 selectinload(CharacterWeapon.weapon).selectinload(Weapon.weapon_specialization),
                 selectinload(CharacterWeapon.weapon).selectinload(Weapon.weapon_traits),
                 selectinload(CharacterWeapon.weapon).selectinload(Weapon.currency),
                 selectinload(CharacterWeapon.weapon).selectinload(Weapon.damage_type),
                 selectinload(CharacterWeapon.weapon).selectinload(Weapon.second_damage_type))
    )


async def character_weapon_create(
        session: AsyncSession,
        character_weapon_in: CharacterWeaponCreateUpdate
) -> CharacterWeapon:
    character = await get_model_result(model=Character, object_id=character_weapon_in.character_id, session=session)
    weapon = await get_model_result(model=Weapon, object_id=character_weapon_in.weapon_id, session=session)
    character_weapon = CharacterWeapon(
        weapon=weapon,
        character=character,
        quantity=character_weapon_in.quantity
    )
    session.add(character_weapon)
    await session.commit()
    await session.refresh(character_weapon)
    return await character_weapon_detail(session=session, character_weapon_id=character_weapon.id)


async def character_weapon_update(
        session: AsyncSession,
        character_weapon_update: CharacterWeaponCreateUpdate,
        character_weapon: CharacterWeapon
):
    weapon = await get_model_result(model=Weapon, object_id=character_weapon_update.weapon_id, session=session)
    setattr(character_weapon, 'quantity', character_weapon_update.quantity)
    character_weapon.weapon = weapon
    await session.commit()
    await session.refresh(character_weapon)
    return character_weapon


async def character_weapon_delete(
        session: AsyncSession,
        character_weapon: CharacterWeapon
):
    await session.delete(character_weapon)
    await session.commit()


async def character_worn_list(session: AsyncSession):
    stmt = select(CharacterWorn).options(
        selectinload(CharacterWorn.character),
        selectinload(CharacterWorn.worn).selectinload(Worn.currency),
        selectinload(CharacterWorn.worn).selectinload(Worn.slot),
        selectinload(CharacterWorn.worn).selectinload(Worn.worn_traits)
    ).order_by(CharacterWorn.id)
    result: Result = await session.execute(stmt)
    worn_list = result.scalars().all()
    return list(worn_list)


async def character_worn_detail(session: AsyncSession, character_worn_id: int) -> CharacterWorn | None:
    return await session.scalar(
        select(CharacterWorn)
        .where(CharacterWorn.id == character_worn_id)
        .options(selectinload(CharacterWorn.character),
                 selectinload(CharacterWorn.worn).selectinload(Worn.currency),
                 selectinload(CharacterWorn.worn).selectinload(Worn.slot),
                 selectinload(CharacterWorn.worn).selectinload(Worn.worn_traits))
    )


async def character_worn_create(
        session: AsyncSession,
        character_worn_in: CharacterWornCreateUpdate
) -> CharacterWorn:
    character = await get_model_result(model=Character, object_id=character_worn_in.character_id, session=session)
    worn = await get_model_result(model=Worn, object_id=character_worn_in.worn_id, session=session)
    character_worn = CharacterWorn(
        worn=worn,
        character=character,
        quantity=character_worn_in.quantity
    )
    session.add(character_worn)
    await session.commit()
    await session.refresh(character_worn)
    return await character_worn_detail(session=session, character_worn_id=character_worn.id)


async def character_worn_update(
        session: AsyncSession,
        character_worn_update: CharacterWornCreateUpdate,
        character_worn: CharacterWorn
):
    worn = await get_model_result(model=Worn, object_id=character_worn_update.worn_id, session=session)
    setattr(character_worn, 'quantity', character_worn_update.quantity)
    character_worn.worn = worn
    await session.commit()
    await session.refresh(character_worn)
    return character_worn


async def character_worn_delete(
        session: AsyncSession,
        character_worn: CharacterWorn
):
    await session.delete(character_worn)
    await session.commit()
