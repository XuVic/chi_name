"""create names table

Revision ID: a5342b4540f5
Revises: b0a2b7d7b157
Create Date: 2019-11-11 10:12:00.857694

"""
from alembic import op
import sqlalchemy as sa
from app.models.columns import uuid, timestamp

# revision identifiers, used by Alembic.
revision = 'a5342b4540f5'
down_revision = 'b0a2b7d7b157'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'names',
        uuid(),
        sa.Column('category', sa.String(10)),
        sa.Column('traditional', sa.String(10)),
        sa.Column('englished', sa.String(10)),
        sa.Column('tf', sa.Integer)
    )


def downgrade():
    op.drop_table('names')
