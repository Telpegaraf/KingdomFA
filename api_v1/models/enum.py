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


class ModelDescription(str, Enum):
    skills = 'skills'
    weapon_mastery = 'weapon_mastery'
    feat_trait = 'feat_trait'


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


model_mapping = {
    "damage_type": models.DamageType,
    "action": models.Action,
    'prerequisite': models.Prerequisite,
    'requirements': models.Requirements,
    'trigger': models.Trigger,
    'title': models.Title
}

model_description_mapping = {
    'skills': models.Skills,
    'weapon_mastery': models.WeaponMastery,
    'feat_trait': models.FeatTrait
}

model_name_description_mapping = {**model_mapping, **model_description_mapping}