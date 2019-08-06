"""movie table

Revision ID: 53e7f117ce0e
Revises: 
Create Date: 2019-08-03 23:14:48.115956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53e7f117ce0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies__database',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movies__database_name'), 'movies__database', ['name'], unique=False)
    op.create_index(op.f('ix_movies__database_score'), 'movies__database', ['score'], unique=False)
    op.create_index(op.f('ix_movies__database_type'), 'movies__database', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_movies__database_type'), table_name='movies__database')
    op.drop_index(op.f('ix_movies__database_score'), table_name='movies__database')
    op.drop_index(op.f('ix_movies__database_name'), table_name='movies__database')
    op.drop_table('movies__database')
    # ### end Alembic commands ###