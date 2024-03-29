"""add col to names

Revision ID: 529e46d008ff
Revises: 0254b8a06fc1
Create Date: 2019-11-11 11:38:56.353487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '529e46d008ff'
down_revision = '0254b8a06fc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('names', sa.Column('simplified', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('names', 'simplified')
    # ### end Alembic commands ###
