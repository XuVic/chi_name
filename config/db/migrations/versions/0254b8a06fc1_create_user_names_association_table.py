"""create user_names association table

Revision ID: 0254b8a06fc1
Revises: a5342b4540f5
Create Date: 2019-11-11 10:12:18.337692

"""
from alembic import op
import sqlalchemy as sa
from app.models.columns import uuid, timestamp

# revision identifiers, used by Alembic.
revision = '0254b8a06fc1'
down_revision = 'a5342b4540f5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users', 
        uuid(),
        sa.Column('messenger_id', sa.String(100), index=True)
    )


def downgrade():
    op.drop_table('users')
