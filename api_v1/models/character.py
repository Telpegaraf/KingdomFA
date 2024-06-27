from sqlalchemy import String, Integer, Text, CheckConstraint, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from api_v1.models.base_model import Base
from api_v1.models.mixins.race import RaceRelationMixin
from api_v1.models.mixins.user import UserRelationMixin
from api_v1.models.mixins.character_class import CharacterClassMixin
from api_v1.models.mixins.god import GodMixin, DomainMixin


class Character(
    RaceRelationMixin,
    UserRelationMixin,
    CharacterClassMixin,
    GodMixin,
    DomainMixin,
    Base
):
    _user_back_populate = "characters"
    _race_back_populate = "characters"
    _character_class_back_populate = "characters"
    _god_back_populate = "characters"
    _domain_back_populate = "characters"
    _domain_id_nullable = True
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100), nullable=True)
    alias: Mapped[str] = mapped_column(String(100), nullable=True)
    age: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    size: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    level: Mapped[int] = mapped_column(SmallInteger, default=1)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    def __str__(self):
        name = self.first_name
        if self.last_name:
            name += f" {self.last_name}"
        if self.alias:
            name += f" {self.alias}"

        return f"{self.__class__.__name__}(id={self.id}, name={name!r})"

    def __repr__(self):
        return self.__str__()
