from sqlalchemy import String, Integer, Text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from api_v1.models.base_model import Base
from api_v1.models.mixins.race import RaceRelationMixin
from api_v1.models.mixins.user import UserRelationMixin


class Character(RaceRelationMixin, UserRelationMixin, Base):
    _user_back_populate = "characters"
    _race_back_populate = "characters"
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    alias: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]
    level: Mapped[int] = mapped_column(Integer, CheckConstraint('level >= 1 AND level <= 20'), default=1)
    description: Mapped[str] = mapped_column(Text)
