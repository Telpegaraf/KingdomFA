from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

import database
from api_v1.models.spell import Spell
from api_v1.schemas import spell as schemas
from api_v1.crud import spell as crud
from api_v1.dependencies.spell import get_spell
from database import db_helper


http_bearer = HTTPBearer()

spell_router = APIRouter(prefix="/spell", tags=["Spell"])


spell_router.get(
    "/{spell_id}/",
    description="Return the Spell object, depending on ID",
    response_model=schemas.SpellRead
)
async def spell_detail(
        spell: Spell = Depends(get_spell),
) -> Spell:
    return spell


@spell_router.get(
    "/",
    description="Return all Spell objects",
    response_model=list[schemas.Spell]
)
async def spell_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[Spell]:
    return await crud.spell_list(session=session)


@spell_router.post(
    "/create/{spell_id}/",
    description="Create a new Spell object",
    response_model=schemas.SpellRead,
    status_code=status.HTTP_201_CREATED
)
async def spell_create(
        spell_in: schemas.SpellCreate,
        spell: Spell = Depends(get_spell),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Spell:
    return await crud.spell_create(session=session, spell=spell, spell_in=spell_in)


@spell_router.patch(
    "update/{spell_id}/",
    description="Update the Spell object, depending on ID",
    response_model=schemas.SpellRead
)
async def spell_update(
        spell_update: schemas.SpellUpdate,
        spell: Spell = Depends(get_spell),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Spell:
    return await crud.spell_update(session=session, spell=spell, spell_update=spell_update)


@spell_router.delete(
    "delete/{spell_id}/",
    description="Delete the Spell object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def spell_delete(
        spell: Spell = Depends(get_spell),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.spell_delete(session=session, spell=spell)
