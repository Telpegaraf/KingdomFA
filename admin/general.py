from sqladmin import ModelView

from kingdom.models.general import (
    DamageType,
    Title,
    Action,
    Prerequisite,
    Requirement,
    Trigger,
    Skill,
    WeaponMastery,
    FeatTrait,
    SpellCast,
    SpellTradition,
    SpellSchool,
    SpellTrait,
    ArmorTrait,
    ArmorSpecialization,
    WeaponTrait,
    WeaponGroup,
    WeaponSpecialization,
    WornTrait
)


class DamageTypeAdmin(ModelView, model=DamageType):
    column_list = [DamageType.id, DamageType.name]
    form_columns = [DamageType.name]
    column_details_list = [DamageType.name]


class TitleAdmin(ModelView, model=Title):
    column_list = [Title.id, Title.name]
    form_columns = [Title.name]


class ActionAdmin(ModelView, model=Action):
    column_list = [Action.id, Action.name]
    form_columns = [Action.name]
    column_details_list = [Action.id, Action.name]


class PrerequisiteAdmin(ModelView, model=Prerequisite):
    column_list = [Prerequisite.id, Prerequisite.name]
    form_columns = [Prerequisite.name]
    column_details_list = [Prerequisite.id, Prerequisite.name]


class RequirementAdmin(ModelView, model=Requirement):
    column_list = [Requirement.id, Requirement.name]
    form_columns = [Requirement.name]
    column_details_list = [Requirement.id, Requirement.name]


class TriggerAdmin(ModelView, model=Trigger):
    column_list = [Trigger.id, Trigger.name]
    form_columns = [Trigger.name]
    column_details_list = [Trigger.id, Trigger.name]


class SkillAdmin(ModelView, model=Skill):
    column_list = [Skill.id, Skill.name]
    form_columns = [Skill.name, Skill.description]
    column_details_list = [Skill.id, Skill.name, Skill.description]


class WeaponMasteryAdmin(ModelView, model=WeaponMastery):
    column_list = [WeaponMastery.id, WeaponMastery.name]
    form_columns = [WeaponMastery.name, WeaponMastery.description]
    column_details_list = [WeaponMastery.id, WeaponMastery.name, WeaponMastery.description]


class FeatTraitAdmin(ModelView, model=FeatTrait):
    column_list = [FeatTrait.id, FeatTrait.name]
    form_columns = [FeatTrait.name, FeatTrait.description]
    column_details_list = [FeatTrait.id, FeatTrait.name, FeatTrait.description]


class SpellCastAdmin(ModelView, model=SpellCast):
    column_list = [SpellCast.id, SpellCast.name]
    form_columns = [SpellCast.name]
    column_details_list = [SpellCast.id, SpellCast.name]


class SpellTraditionAdmin(ModelView, model=SpellTradition):
    column_list = [SpellTradition.id, SpellTradition.name]
    form_columns = [SpellTradition.name, SpellTradition.description]
    column_details_list = [SpellTradition.id, SpellTradition.name, SpellTradition.description]


class SpellSchoolAdmin(ModelView, model=SpellSchool):
    column_list = [SpellSchool.id, SpellSchool.name]
    form_columns = [SpellSchool.name, SpellSchool.description]
    column_details_list = [SpellSchool.id, SpellSchool.name, SpellSchool.description]


class SpellTraitAdmin(ModelView, model=SpellTrait):
    column_list = [SpellTrait.id, SpellTrait.name]
    form_columns = [SpellTrait.name, SpellTrait.description]
    column_details_list = [SpellTrait.id, SpellTrait.name, SpellTrait.description]


class ArmorTraitAdmin(ModelView, model=ArmorTrait):
    column_list = [ArmorTrait.id, ArmorTrait.name]
    form_columns = [ArmorTrait.name, ArmorTrait.description]
    column_details_list = [ArmorTrait.id, ArmorTrait.name, ArmorTrait.description]


class ArmorSpecializationAdmin(ModelView, model=ArmorSpecialization):
    column_list = [ArmorSpecialization.id, ArmorSpecialization.name]
    form_columns = [ArmorSpecialization.name, ArmorSpecialization.description]
    column_details_list = [ArmorSpecialization.id, ArmorSpecialization.name, ArmorSpecialization.description]


class WeaponTraitAdmin(ModelView, model=WeaponTrait):
    column_list = [WeaponTrait.id, WeaponTrait.name]
    form_columns = [WeaponTrait.name, WeaponTrait.description]
    column_details_list = [WeaponTrait.id, WeaponTrait.name, WeaponTrait.description]


class WeaponGroupAdmin(ModelView, model=WeaponGroup):
    column_list = [WeaponGroup.id, WeaponGroup.name]
    form_columns = [WeaponGroup.name, WeaponGroup.description]
    column_details_list = [WeaponGroup.id, WeaponGroup.name, WeaponGroup.description]


class WeaponSpecializationAdmin(ModelView, model=WeaponSpecialization):
    column_list = [WeaponSpecialization.id, WeaponSpecialization.name]
    form_columns = [WeaponSpecialization.name, WeaponSpecialization.description]
    column_details_list = [WeaponSpecialization.id, WeaponSpecialization.name, WeaponSpecialization.description]


class WornTraitAdmin(ModelView, model=WornTrait):
    column_list = [WornTrait.id, WornTrait.name]
    form_columns = [WornTrait.name, WornTrait.description]
    column_details_list = [WornTrait.id, WornTrait.name, WornTrait.description]
