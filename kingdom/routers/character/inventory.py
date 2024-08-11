from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from kingdom.models.inventory import CharacterCurrency, CharacterWorn, CharacterArmor, CharacterWeapon, CharacterItem
from kingdom.schemas.character import inventory as schemas
from kingdom.crud.character import inventory as crud
from kingdom.dependencies.character.inventory import (
    get_character_currency,
    get_character_item,
    get_character_armor,
    get_character_weapon,
    get_character_worn
)
from database import db_helper


http_bearer = HTTPBearer()

inventory_router = APIRouter(prefix="/inventory", tags=["Inventory"])


# Character Currency Routers
@inventory_router.get(
    "/character_currency/{character_currency_id}/",
    description="Return the Character Currency object, depending on ID",
    response_model=schemas.CharacterCurrencyRead
)
async def character_currency_detail(character: CharacterCurrency = Depends(get_character_currency)) -> CharacterCurrency:
    return character


@inventory_router.get(
    "/character_currency/",
    description="Return all Character Currency objects",
    response_model=list[schemas.CharacterCurrency]
)
async def character_currency_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterCurrency]:
    return await crud.character_currency_list(session=session)


@inventory_router.post(
    "/character_currency/",
    description="Create a new Character Currency object",
    response_model=schemas.CharacterCurrencyRead,
    status_code=status.HTTP_201_CREATED
)
async def character_currency_create(
        character_currency_in: schemas.CharacterCurrencyCreateUpdate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterCurrency:
    return await crud.character_currency_create(session=session, character_currency_in=character_currency_in)


@inventory_router.patch(
    "/character_currency/{character_currency_id}/",
    description="Update the Character Currency object, depending on ID",
    response_model=schemas.CharacterCurrencyCreateUpdate
)
async def character_currency_update(
        character_currency_update: schemas.CharacterCurrencyCreateUpdate,
        character_currency: CharacterCurrency = Depends(get_character_currency),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterCurrency:
    return await crud.character_currency_update(session=session, character_currency=character_currency,
                                                character_currency_update=character_currency_update)


@inventory_router.delete(
    "/character_currency/{character_currency_id}/",
    description="Delete the Character Point object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_currency_delete(
        character_currency: CharacterCurrency = Depends(get_character_currency),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_currency_delete(session=session, character_currency=character_currency)


# Character Item routers
@inventory_router.get(
    "/character_item/{character_item_id}/",
    description="Return the Character Item object, depending on ID",
    response_model=schemas.CharacterItemRead
)
async def character_item_detail(character_item: CharacterItem = Depends(get_character_item)) -> CharacterItem:
    return character_item


@inventory_router.get(
    "/character_item/",
    description="Return all Character Item objects",
    response_model=list[schemas.CharacterItem]
)
async def character_item_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterItem]:
    return await crud.character_item_list(session=session)


@inventory_router.post(
    "/character_item/",
    description="Create a new Character Item object",
    response_model=schemas.CharacterItemRead,
    status_code=status.HTTP_201_CREATED
)
async def character_item_create(
        character_item_in: schemas.CharacterItemCreateUpdate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterItem:
    return await crud.character_item_create(session=session, character_item_in=character_item_in)


@inventory_router.patch(
    "/character_item/{character_item_id}/",
    description="Update the Character Item object, depending on ID",
    response_model=schemas.CharacterItemCreateUpdate
)
async def character_item_update(
        character_item_update: schemas.CharacterItemCreateUpdate,
        character_item: CharacterItem = Depends(get_character_item),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterItem:
    return await crud.character_item_update(session=session, character_item=character_item,
                                            character_item_update=character_item_update)


@inventory_router.delete(
    "/character_item/{character_item_id}/",
    description="Delete the Character Item object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_item_delete(
        character_item: CharacterItem = Depends(get_character_item),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_item_delete(session=session, character_item=character_item)


# Character Armor routers
@inventory_router.get(
    "/character_armor/{character_armor_id}/",
    description="Return the Character Armor object, depending on ID",
    response_model=schemas.CharacterArmorRead
)
async def character_armor_detail(character_armor: CharacterArmor = Depends(get_character_armor)) -> CharacterArmor:
    return character_armor


@inventory_router.get(
    "/character_armor/",
    description="Return all Character Armor objects",
    response_model=list[schemas.CharacterArmor]
)
async def character_armor_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterArmor]:
    return await crud.character_armor_list(session=session)


@inventory_router.post(
    "/character_armor/",
    description="Create a new Character Armor object",
    response_model=schemas.CharacterArmorRead,
    status_code=status.HTTP_201_CREATED
)
async def character_armor_create(
        character_armor_in: schemas.CharacterArmorCreateUpdate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterArmor:
    return await crud.character_armor_create(session=session, character_armor_in=character_armor_in)


@inventory_router.patch(
    "/character_armor/{character_armor_id}/",
    description="Update the Character Armor object, depending on ID",
    response_model=schemas.CharacterArmorCreateUpdate
)
async def character_armor_update(
        character_armor_update: schemas.CharacterArmorCreateUpdate,
        character_armor: CharacterArmor = Depends(get_character_armor),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterArmor:
    return await crud.character_armor_update(session=session, character_armor=character_armor,
                                             character_armor_update=character_armor_update)


@inventory_router.delete(
    "/character_armor/{character_armor_id}/",
    description="Delete the Character Armor object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_armor_delete(
        character_armor: CharacterArmor = Depends(get_character_armor),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_armor_delete(session=session, character_armor=character_armor)


# Character Weapon routers
@inventory_router.get(
    "/character_weapon/{character_weapon_id}/",
    description="Return the Character Weapon object, depending on ID",
    response_model=schemas.CharacterWeaponRead
)
async def character_weapon_detail(
        character_weapon: CharacterWeapon = Depends(get_character_weapon)
) -> CharacterWeapon:
    return character_weapon


@inventory_router.get(
    "/character_weapon/",
    description="Return all Character Weapon objects",
    response_model=list[schemas.CharacterWeapon]
)
async def character_weapon_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterWeapon]:
    return await crud.character_weapon_list(session=session)


@inventory_router.post(
    "/character_weapon/",
    description="Create a new Character Weapon object",
    response_model=schemas.CharacterWeaponRead,
    status_code=status.HTTP_201_CREATED
)
async def character_weapon_create(
        character_weapon_in: schemas.CharacterWeaponCreateUpdate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterWeapon:
    return await crud.character_weapon_create(session=session, character_weapon_in=character_weapon_in)


@inventory_router.patch(
    "/character_weapon/{character_weapon_id}/",
    description="Update the Character Weapon object, depending on ID",
    response_model=schemas.CharacterWeaponCreateUpdate
)
async def character_weapon_update(
        character_weapon_update: schemas.CharacterWeaponCreateUpdate,
        character_weapon: CharacterWeapon = Depends(get_character_weapon),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterWeapon:
    return await crud.character_weapon_update(session=session, character_weapon=character_weapon,
                                              character_weapon_update=character_weapon_update)


@inventory_router.delete(
    "/character_weapon/{character_weapon_id}/",
    description="Delete the Character Weapon object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_weapon_delete(
        character_weapon: CharacterWeapon = Depends(get_character_weapon),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_weapon_delete(session=session, character_weapon=character_weapon)


# Character Worn routers
@inventory_router.get(
    "/character_worn/{character_worn_id}/",
    description="Return the Character Worn object, depending on ID",
    response_model=schemas.CharacterWornRead
)
async def character_worn_detail(
        character_worn: CharacterWorn = Depends(get_character_worn)
) -> CharacterWorn:
    return character_worn


@inventory_router.get(
    "/character_worn/",
    description="Return all Character Worn objects",
    response_model=list[schemas.CharacterWorn]
)
async def character_worn_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterWorn]:
    return await crud.character_worn_list(session=session)


@inventory_router.post(
    "/character_worn/",
    description="Create a new Character Worn object",
    response_model=schemas.CharacterWornRead,
    status_code=status.HTTP_201_CREATED
)
async def character_worn_create(
        character_worn_in: schemas.CharacterWornCreateUpdate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterWorn:
    return await crud.character_worn_create(session=session, character_worn_in=character_worn_in)


@inventory_router.patch(
    "/character_worn/{character_worn_id}/",
    description="Update the Character Worn object, depending on ID",
    response_model=schemas.CharacterWornCreateUpdate
)
async def character_worn_update(
        character_worn_update: schemas.CharacterWornCreateUpdate,
        character_worn: CharacterWorn = Depends(get_character_worn),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterWorn:
    return await crud.character_worn_update(session=session, character_worn=character_worn,
                                            character_worn_update=character_worn_update)


@inventory_router.delete(
    "/character_worn/{character_worn_id}/",
    description="Delete the Character Worn object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_worn_delete(
        character_worn: CharacterWorn = Depends(get_character_worn),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_worn_delete(session=session, character_worn=character_worn)
