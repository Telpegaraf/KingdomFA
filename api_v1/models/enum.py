from enum import Enum
from api_v1.models import general as models


class MasteryLevels(Enum):
    ABSENT = 'None',
    TRAIN = 'Train',
    EXPERT = 'Expert',
    MASTER = 'Master',
    LEGEND = 'Legend'


class ArmorCategory(Enum):
    UNARMED = 'Unarmed',
    LIGHT = 'Light',
    MEDIUM = 'Medium',
    HEAVY = 'Heavy'


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
    spell_component = 'spell_component'


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
    spell_component = 'spell_component'


model_mapping = {
    "damage_type": models.DamageType,
    "action": models.Action,
    'prerequisite': models.Prerequisite,
    'requirements': models.Requirements,
    'trigger': models.Trigger,
    'title': models.Title,
    'spell_cast': models.SpellCast
}

model_description_mapping = {
    'skills': models.Skills,
    'weapon_mastery': models.WeaponMastery,
    'feat_trait': models.FeatTrait,
    'spell_tradition': models.SpellTradition,
    'spell_school': models.SpellSchool,
    'spell_trait': models.SpellTrait,
    'spell_component': models.SpellComponent,
}

model_name_description_mapping = {**model_mapping, **model_description_mapping}