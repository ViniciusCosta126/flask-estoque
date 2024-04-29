"""Criando relacionamente entre unidade e produto

Revision ID: f596e16181e8
Revises: 20052c1e82d9
Create Date: 2024-04-29 12:27:16.145812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f596e16181e8'
down_revision = '20052c1e82d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unidades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('produtos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unidade_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'unidades', ['unidade_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produtos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('unidade_id')

    op.drop_table('unidades')
    # ### end Alembic commands ###
