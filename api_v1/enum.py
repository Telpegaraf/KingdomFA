from enum import Enum


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
