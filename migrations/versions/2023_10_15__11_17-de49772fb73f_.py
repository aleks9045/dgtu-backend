"""empty message

Revision ID: de49772fb73f
Revises: 9a85d0559260
Create Date: 2023-10-15 11:17:33.198591

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_file


# revision identifiers, used by Alembic.
revision: str = 'de49772fb73f'
down_revision: Union[str, None] = '9a85d0559260'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###