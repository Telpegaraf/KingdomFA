from contextlib import asynccontextmanager
from fastapi import FastAPI

from api_v1.routers import religion, user, auth, general, character_class, user_test, spell, race
from api_v1.routers.equipment import worn, armor, weapon
from api_v1.routers.character import character, character_stat, character_point, secondary_stat,\
    character_weapon_mastery, character_skill_mastery
from action.create_superuser import create_superuser

app = FastAPI()
app.include_router(auth.auth_router)
app.include_router(user.user_router)
app.include_router(character.character_router)
app.include_router(character_stat.character_stats_router)
app.include_router(character_point.character_point_router)
app.include_router(secondary_stat.secondary_stat_router)
app.include_router(character_skill_mastery.character_skill_mastery_router)
app.include_router(character_weapon_mastery.character_weapon_mastery_router)
app.include_router(religion.religion_router)
app.include_router(general.general_router)
app.include_router(character_class.character_class_router)
app.include_router(worn.worn_router)
app.include_router(armor.armor_router)
app.include_router(weapon.weapon_router)
app.include_router(user_test.auth_router)
app.include_router(spell.spell_router)
app.include_router(race.race_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_superuser()
    yield
