"""empty message

Revision ID: e85ae82e159f
Revises: a8118e4beb78
Create Date: 2017-12-24 13:29:44.720956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e85ae82e159f'
down_revision = 'a8118e4beb78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('types', sa.Column('order', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('types', 'order')
    # ### end Alembic commands ###