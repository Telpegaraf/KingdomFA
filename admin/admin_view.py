from sqladmin import Admin

from admin.admin_panel import AdminAuth
from admin.general import (
    DamageTypeAdmin,
    TitleAdmin,
    ActionAdmin,
    PrerequisiteAdmin,
    RequirementAdmin,
    TriggerAdmin,
    SkillAdmin,
    WeaponMasteryAdmin,
    FeatTraitAdmin,
    SpellCastAdmin,
    SpellTraitAdmin,
    SpellSchoolAdmin,
    SpellTraditionAdmin,
    WeaponSpecializationAdmin,
    WeaponGroupAdmin,
    WeaponTraitAdmin,
    WornTraitAdmin,
    ArmorTraitAdmin,
    ArmorSpecializationAdmin
)
from admin.user import UserAdmin
from admin.religion import DomainAdmin, GodAdmin
from core.config import settings
from database import db_helper


def create_admin(app):
    authentication_backend = AdminAuth(secret_key=settings.get_secret_key)
    admin = Admin(app=app, engine=db_helper.engine, authentication_backend=authentication_backend)
    admin.add_view(UserAdmin)
    admin.add_view(DomainAdmin)
    admin.add_view(GodAdmin)
    admin.add_view(DamageTypeAdmin)
    admin.add_view(TitleAdmin)
    admin.add_view(ActionAdmin)
    admin.add_view(PrerequisiteAdmin)
    admin.add_view(RequirementAdmin)
    admin.add_view(TriggerAdmin)
    admin.add_view(SkillAdmin)
    admin.add_view(WeaponTraitAdmin)
    admin.add_view(WeaponSpecializationAdmin)
    admin.add_view(WeaponGroupAdmin)
    admin.add_view(WeaponMasteryAdmin)
    admin.add_view(FeatTraitAdmin)
    admin.add_view(SpellSchoolAdmin)
    admin.add_view(SpellTraditionAdmin)
    admin.add_view(SpellTraitAdmin)
    admin.add_view(SpellCastAdmin)
    admin.add_view(WornTraitAdmin)
    admin.add_view(ArmorSpecializationAdmin)
    admin.add_view(ArmorTraitAdmin)

    return admin
