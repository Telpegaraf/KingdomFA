import inflection
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class MainBase(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return inflection.tableize(cls.__name__)


class Base(MainBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
