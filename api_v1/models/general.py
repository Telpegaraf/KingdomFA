from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from api_v1.models import Base


class GeneralBase(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(500), unique=True, index=True)

    @declared_attr.directive
    def __str__(self):
        return f"{self.__class__.name}(id={self.id}, name={self.name!r})"

    @declared_attr.directive
    def __repr__(self):
        return self.name


class GeneralDescriptionBase(Base):
    __abstract__ = True
    description: Mapped[str] = mapped_column(String(500))


class DamageType(GeneralBase):
    pass


class Title(GeneralBase):
    pass


class Action(GeneralBase):
    pass


class Prerequisite(GeneralBase):
    pass


class Requirements(GeneralBase):
    pass


class Trigger(GeneralBase):
    pass


class Skills(GeneralDescriptionBase):
    pass


class WeaponMastery(GeneralDescriptionBase):
    pass


class FeatTrait(GeneralDescriptionBase):
    pass
