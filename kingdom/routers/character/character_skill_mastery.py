from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from kingdom.models.character import CharacterSkillMastery
from kingdom.schemas.character import character_skill_mastery as schemas
from kingdom.crud.character import character_skill_mastery as crud
from kingdom.dependencies.character.character_skill_mastery import get_character_skill_mastery
from database import db_helper


http_bearer = HTTPBearer()

character_skill_mastery_router = APIRouter(prefix="/character_skill_mastery", tags=["Character Skill"])


@character_skill_mastery_router.get(
    "/{character_skill_mastery_id}/",
    description="Return the Character Skill Mastery object, depending on ID",
    response_model=schemas.CharacterSkillMasteryRead
)
async def character_skill_mastery_detail(
        character: CharacterSkillMastery = Depends(get_character_skill_mastery)
) -> CharacterSkillMastery:
    return character


@character_skill_mastery_router.get(
    "/",
    description="Return all Character Skill Mastery objects",
    response_model=list[schemas.CharacterSkillMastery]
)
async def character_skill_mastery_list(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[CharacterSkillMastery]:
    return await crud.character_skill_mastery_list(session=session)


@character_skill_mastery_router.post(
    "/create/",
    description="Create a new Character Skill Mastery object",
    response_model=schemas.CharacterSkillMasteryRead,
    status_code=status.HTTP_201_CREATED
)
async def character_skill_mastery_create(
        character_skill_mastery_in: schemas.CharacterSkillMasteryCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterSkillMastery:
    return await crud.character_skill_mastery_create(
        session=session,
        character_skill_mastery_in=character_skill_mastery_in
    )


@character_skill_mastery_router.patch(
    "/update/{character_skill_mastery_id}/",
    description="Update the Character Skill Mastery object, depending on ID",
    response_model=schemas.CharacterSkillMasteryRead
)
async def character_update(
        character_skill_mastery_update: schemas.CharacterSkillMasteryUpdate,
        character_skill_mastery: CharacterSkillMastery = Depends(get_character_skill_mastery),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> CharacterSkillMastery:
    return await crud.character_stats_update(session=session, character_skill_mastery=character_skill_mastery,
                                             character_skill_mastery_update=character_skill_mastery_update)


@character_skill_mastery_router.delete(
    "/delete/{character_skill_mastery_id}/",
    description="Delete the Character Skill Mastery object, depending on ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def character_skill_mastery_delete(
        character: CharacterSkillMastery = Depends(get_character_skill_mastery),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.character_skill_mastery_delete(session=session, character=character)
