"""add content table to post table

Revision ID: cfe3a314e953
Revises: af9e10615617
Create Date: 2024-03-20 17:46:06.679038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'cfe3a314e953'
down_revision: Union[str, None] = 'af9e10615617'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
