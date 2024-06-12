from sqlalchemy import Table, Column, ForeignKey
from api_v1.models.base_model import Base


god_domain_association = Table(
    'god_domain',
    Base.metadata,
    Column('god_id', ForeignKey('gods.id'), primary_key=True),
    Column('domain_id', ForeignKey('domains.id'), primary_key=True)
)
