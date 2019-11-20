import sqlalchemy as sa
from sqlalchemy.orm import relationship
from .columns import uuid

from . import Base
from . import user_names

class Name(Base):
    __tablename__ = 'names'

    uuid = uuid()
    category = sa.Column(sa.String(10))
    traditional = sa.Column(sa.String(10))
    simplified = sa.Column(sa.String(10))
    englished = sa.Column(sa.String(10))
    tf = sa.Column(sa.Integer)
    users = relationship("User", secondary=user_names, back_populates='names')
    