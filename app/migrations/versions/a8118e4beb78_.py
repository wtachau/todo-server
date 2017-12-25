"""empty message

Revision ID: a8118e4beb78
Revises: eae2507bae41
Create Date: 2017-12-24 13:17:51.699044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8118e4beb78'
down_revision = 'eae2507bae41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'entries', sa.Column('type_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'entries', 'types', ['type_id'], ['id'])
    op.drop_column(u'entries', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'entries', sa.Column('type', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'entries', type_='foreignkey')
    op.drop_column(u'entries', 'type_id')
    op.drop_table('types')
    # ### end Alembic commands ###