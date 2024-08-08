from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from kingdom.models.general import Skill


class SkillMixin:
    _skill_id_nullable: bool = False
    _skill_id_unique: bool = False
    _skill_back_populate: str | None = None

    @declared_attr
    def skill_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(
                "skills.id", ondelete="CASCADE"
            ),
            nullable=cls._skill_id_nullable,
            unique=cls._skill_id_unique
        )

    @declared_attr
    def skill(cls) -> Mapped["Skill"]:
        return relationship(
            back_populates=cls._skill_back_populate
        )
