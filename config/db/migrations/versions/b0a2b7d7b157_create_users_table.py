"""create users table

Revision ID: b0a2b7d7b157
Revises: 
Create Date: 2019-11-11 10:11:53.374314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0a2b7d7b157'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_names',
        sa.Column('user_id', sa.String(100), sa.ForeignKey('users.uuid'), primary_key=True),
        sa.Column('name_id', sa.String(100), sa.ForeignKey('names.uuid'), primary_key=True)
    )


def downgrade():
    op.drop_table('user_names')
