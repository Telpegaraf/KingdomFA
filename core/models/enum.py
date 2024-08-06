from enum import Enum
from core.models import general as models
from core.models import equipment


class MasteryLevels(str, Enum):
    ABSENT = 'None'
    TRAIN = 'Train'
    EXPERT = 'Expert'
    MASTER = 'Master'
    LEGEND = 'Legend'


class HealthByLevel(int, Enum):
    SIX = 6
    EIGHT = 8
    TEN = 10
    TWELVE = 12


class ModelName(str, Enum):
    damage_type = 'damage_type'
    action = 'action'
    prerequisite = 'prerequisite'
    requirements = 'requirements'
    trigger = 'trigger'
    title = 'title'
    spell_cast = 'spell_cast'


class ModelDescription(str, Enum):
    skills = 'skills'
    weapon_mastery = 'weapon_mastery'
    feat_trait = 'feat_trait'
    spell_tradition = 'spell_tradition'
    spell_school = 'spell_school'
    spell_trait = 'spell_trait'
    armor_trait = 'armor_trait'
    armor_specialization = 'armor_specialization'
    weapon_trait = 'weapon_trait'
    weapon_group = 'weapon_group'
    weapon_specialization = 'weapon_specialization'
    worn_trait = 'worn_trait'


class ModelNameDescription(str, Enum):
    damage_type = 'damage_type'
    action = 'action'
    prerequisite = 'prerequisite'
    requirements = 'requirements'
    trigger = 'trigger'
    title = 'title'
    skills = 'skills'
    weapon_mastery = 'weapon_mastery'
    feat_trait = 'feat_trait'
    spell_cast = 'spell_cast'
    spell_tradition = 'spell_tradition'
    spell_school = 'spell_school'
    spell_trait = 'spell_trait'
    armor_trait = 'armor_trait'
    armor_specialization = 'armor_specialization'
    weapon_trait = 'weapon_trait'
    weapon_group = 'weapon_group'
    weapon_specialization = 'weapon_specialization'
    worn_trait = 'worn_trait'


model_mapping = {
    "damage_type": models.DamageType,
    "action": models.Action,
    'prerequisite': models.Prerequisite,
    'requirements': models.Requirement,
    'trigger': models.Trigger,
    'title': models.Title,
    'spell_cast': models.SpellCast
}

model_description_mapping = {
    'skills': models.Skill,
    'weapon_mastery': models.WeaponMastery,
    'feat_trait': models.FeatTrait,
    'spell_tradition': models.SpellTradition,
    'spell_school': models.SpellSchool,
    'spell_trait': models.SpellTrait,
    'armor_trait': models.ArmorTrait,
    'armor_specialization': models.ArmorSpecialization,
    'weapon_trait': models.WeaponTrait,
    'weapon_group': models.WeaponGroup,
    'weapon_specialization': models.WeaponSpecialization,
    'worn_trait': models.WornTrait
}

model_name_description_mapping = {**model_mapping, **model_description_mapping}


class EquipmentEnum(str, Enum):
    worn = 'worn'
    ARMOR = 'armor'
    WEAPON = 'weapon'


equipment_model_mapping = {
    'worn': equipment.Worn
}

