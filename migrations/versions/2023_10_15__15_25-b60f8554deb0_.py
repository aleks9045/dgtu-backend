"""empty message

Revision ID: b60f8554deb0
Revises: 3324427f464e
Create Date: 2023-10-15 15:25:00.809639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_file
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b60f8554deb0'
down_revision: Union[str, None] = '3324427f464e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('name', sqlalchemy_file.types.FileField(), nullable=False))
    op.add_column('file', sa.Column('info', sa.String(length=16), nullable=False))
    op.add_column('file', sa.Column('number', sa.Integer(), nullable=True))
    op.drop_column('file', 'file')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('file', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False))
    op.drop_column('file', 'number')
    op.drop_column('file', 'info')
    op.drop_column('file', 'name')
    # ### end Alembic commands ###