from sqlalchemy.orm import mapped_column, Mapped
from core.models import Base


class Domain(Base):
    name: Mapped[str] = mapped_column(index=True)

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
