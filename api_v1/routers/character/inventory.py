from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.models.inventory import CharacterCurrency
from api_v1.schemas.character import inventory as schemas
from api_v1.crud.character import inventory as crud
from api_v1.dependencies.character.inventory import get_character_currency
from database import db_helper


http_bearer = HTTPBearer()

inventory_router = APIRouter(prefix="/inventory", tags=["Inventory"])


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
    "/character_currency/create/",
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
    "/character_currency/update/{character_point_id}/",
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
    "/character_currency/delete/{character_point_id}/",
    description="Delete the Character Point object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_currency_delete(
        character_currency: CharacterCurrency = Depends(get_character_currency),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_currency_delete(session=session, character_currency=character_currency)
