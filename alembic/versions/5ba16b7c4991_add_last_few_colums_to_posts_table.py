"""add last few colums to posts table

Revision ID: 5ba16b7c4991
Revises: 52280912c155
Create Date: 2024-03-22 08:15:47.482098

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5ba16b7c4991'
down_revision: Union[str, None] = '52280912c155'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column('posts', sa.Column("created_at", sa.TIMESTAMP, nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
