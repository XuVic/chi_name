from .columns import uuid
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from . import Base
from . import user_names

class User(Base):
    __tablename__ = 'users'

    uuid = uuid()
    messenger_id = sa.Column(sa.String(100), index=True)
    names = relationship("Name", secondary=user_names, back_populates='users')
    
