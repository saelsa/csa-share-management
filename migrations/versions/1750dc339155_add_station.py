"""add station

Revision ID: 1750dc339155
Revises: 5cc85b66507f
Create Date: 2017-05-05 07:45:58.341855

"""

# revision identifiers, used by Alembic.
revision = '1750dc339155'
down_revision = '5cc85b66507f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('station',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('share', sa.Column('station_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'share', 'station', ['station_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'share', type_='foreignkey')
    op.drop_column('share', 'station_id')
    op.drop_table('station')
    ### end Alembic commands ###
