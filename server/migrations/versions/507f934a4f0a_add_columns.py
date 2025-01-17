"""add columns

Revision ID: 507f934a4f0a
Revises: abd34a0fc6a2
Create Date: 2023-09-07 12:42:51.977834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '507f934a4f0a'
down_revision = 'abd34a0fc6a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
