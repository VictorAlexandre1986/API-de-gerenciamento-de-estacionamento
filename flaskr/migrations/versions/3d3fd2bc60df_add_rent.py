"""Add rent.

Revision ID: 3d3fd2bc60df
Revises: 531f742487dc
Create Date: 2024-06-10 15:04:59.466503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d3fd2bc60df'
down_revision = '531f742487dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alugueis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('plate', sa.String(length=10), nullable=True),
    sa.Column('model', sa.String(length=80), nullable=True),
    sa.Column('rent_date_initial', sa.DateTime(), nullable=True),
    sa.Column('rent_date_final', sa.DateTime(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('alugueis', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_alugueis_id'), ['id'], unique=False)

    op.create_table('token_block_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('token_block_list', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_token_block_list_jti'), ['jti'], unique=False)

    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_id'))

    op.drop_table('users')
    with op.batch_alter_table('token_block_list', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_token_block_list_jti'))

    op.drop_table('token_block_list')
    with op.batch_alter_table('alugueis', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_alugueis_id'))

    op.drop_table('alugueis')
    # ### end Alembic commands ###
