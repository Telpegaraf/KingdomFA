from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models import Base
from api_v1.general.mixins import RaceRelationMixin
from api_v1.user.mixins import UserRelationMixin



class Title(Base):
    name: Mapped[str] = mapped_column(String(50), unique=True)

    def __repr__(self):
        return self.name


class Character(RaceRelationMixin, UserRelationMixin, Base):
    _user_back_populate = "user"
    _race_back_populate = "character"
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    alias: Mapped[str] = mapped_column(String(100))
    #class_character:
    #god: Mapped[int] = mapped_column(
    #    ForeignKey("gods.id")
    #)
    #domain:
    age: Mapped[int]
    level: Mapped[int] = mapped_column(Integer, default=0)
    description: Mapped[str] = mapped_column(Text)
