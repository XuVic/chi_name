from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

Base = declarative_base()

user_names = sa.Table('user_names', Base.metadata, 
    sa.Column('user_id', sa.String(100), sa.ForeignKey('users.uuid'), primary_key=True),
    sa.Column('name_id', sa.String(100), sa.ForeignKey('names.uuid'), primary_key=True)
)

from .user import User
from .name import Name