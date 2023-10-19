"""initial migration

Revision ID: 5e12bbdaaa85
Revises: 
Create Date: 2023-10-18 22:00:09.632349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e12bbdaaa85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('category', sa.Enum('Aviator', 'Wayfarer', 'Round', 'Sports', 'Designer', 'Oversized', 'Cat-Eye'), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=41), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_seller', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('product')
    # ### end Alembic commands ###
