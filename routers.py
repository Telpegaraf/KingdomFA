from fastapi import FastAPI
from kingdom.routers import religion, user, auth, general, character_class, user_test, spell, race
from kingdom.routers.equipment import worn, armor, weapon
from kingdom.routers.character import(
    character,
    character_stat,
    character_point,
    secondary_stat,
    character_weapon_mastery,
    character_skill_mastery,
    inventory
)


def include_routers(app: FastAPI):
    app.include_router(auth.auth_router)
    app.include_router(user.user_router)
    app.include_router(character.character_router)
    app.include_router(character_stat.character_stats_router)
    app.include_router(character_point.character_point_router)
    app.include_router(secondary_stat.secondary_stat_router)
    app.include_router(character_skill_mastery.character_skill_mastery_router)
    app.include_router(character_weapon_mastery.character_weapon_mastery_router)
    app.include_router(inventory.inventory_router)
    app.include_router(religion.religion_router)
    app.include_router(general.general_router)
    app.include_router(character_class.character_class_router)
    app.include_router(worn.worn_router)
    app.include_router(armor.armor_router)
    app.include_router(weapon.weapon_router)
    app.include_router(user_test.auth_router)
    app.include_router(spell.spell_router)
    app.include_router(race.race_router)
