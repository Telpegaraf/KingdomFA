from sqlalchemy import String, Table, Column, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from core.models import Base


god_domain_association = Table(
    'god_domain',
    Base.metadata,
    Column('god_id', ForeignKey('gods.id'), primary_key=True),
    Column('domain_id', ForeignKey('domains.id'), primary_key=True)
)


class Domain(Base):
    name: Mapped[str] = mapped_column(String(50), index=True)
    gods: Mapped[list["God"]] = relationship(
        secondary=god_domain_association,
        back_populates="domains"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name


class God(Base):
    name: Mapped[str] = mapped_column(String(100), index=True)
    alias: Mapped[str] = mapped_column(String(100))
    edict: Mapped[str] = mapped_column(String(300))
    anathema: Mapped[str] = mapped_column(String(300))
    areas_of_interest: Mapped[str] = mapped_column(String(300))
    temples: Mapped[str] = mapped_column(String(300))
    worship: Mapped[str] = mapped_column(String(300))
    sacred_animal: Mapped[str] = mapped_column(String(300))
    sacred_color: Mapped[str] = mapped_column(String(300))
    chosen_weapon: Mapped[str] = mapped_column(String(300))
    taro: Mapped[str] = mapped_column(String(300))
    alignment: Mapped[str] = mapped_column(String(300))
    domains: Mapped[list["Domain"]] = relationship(
        secondary=god_domain_association,
        back_populates="gods"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return self.name

# god_domains = Table(
#     'god_domains',
#     Base.metadata,
#     Column('god_id', Integer, ForeignKey('gods.id')),
#     Column('domais_is', Integer, ForeignKey('domains.id'))
# )
#
#
# class God(Base):
#     __tablename__ = 'gods'
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     alias = Column(String)
#     edict = Column(String)
#     anathema = Column(String)
#     areas_of_interest = Column(String)
#     temples = Column(String)
#     worship = Column(String)
#     sacred_animal = Column(String)
#     sacred_color = Column(String)
#     chosen_weapon = Column(String)
#     taro = Column(String)
#     alignment = Column(String, default="Unknown")
#
#     domain = relationship('Domains', secondary=god_domains, back_populates='gods')
#
#     def __repr__(self):
#         return f"{self.name}, {self.alias}"
#
#
# Domain.gods = relationship('God', secondary=god_domains, back_populates='domain')
