from fastapi import Path, Depends
from annotated_types import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.crud.character.inventory import (
    character_currency_detail,
    character_item_detail,
    character_armor_detail,
    character_weapon_detail,
    character_worn_detail
)
from api_v1.models.inventory import CharacterCurrency, CharacterItem, CharacterArmor, CharacterWeapon, CharacterWorn


async def get_character_currency(
        character_currency_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterCurrency | None:
    return await character_currency_detail(
        session=session,
        character_currency_id=character_currency_id
    )


async def get_character_item(
        character_item_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterItem | None:
    return await character_item_detail(
        session=session,
        character_item_id=character_item_id
    )


async def get_character_armor(
        character_armor_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterArmor | None:
    return await character_armor_detail(
        session=session,
        character_armor_id=character_armor_id
    )


async def get_character_weapon(
        character_weapon_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterWeapon | None:
    return await character_weapon_detail(
        session=session,
        character_weapon_id=character_weapon_id
    )


async def get_character_worn(
        character_worn_id: Annotated[int, Path],
        session: AsyncSession = Depends(database.db_helper.scoped_session_dependency)
) -> CharacterWorn | None:
    return await character_worn_detail(
        session=session,
        character_item_id=character_worn_id
    )
