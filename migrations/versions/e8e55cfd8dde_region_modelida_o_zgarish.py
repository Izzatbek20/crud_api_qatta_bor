"""Region modelida o'zgarish

Revision ID: e8e55cfd8dde
Revises: 81d2b6844d7d
Create Date: 2025-03-19 11:41:20.140272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8e55cfd8dde'
down_revision: Union[str, None] = '81d2b6844d7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('region', sa.Column('parent_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('region', 'parent_id')
    # ### end Alembic commands ###
