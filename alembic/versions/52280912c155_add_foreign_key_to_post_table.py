"""add foreign-key to post table

Revision ID: 52280912c155
Revises: 9e89636205fb
Create Date: 2024-03-21 14:35:53.336925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '52280912c155'
down_revision: Union[str, None] = '9e89636205fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=True))
    op.create_foreign_key("posts_users_fk", "posts",
                          "users", ["owner_id"],
                          ["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_column("posts", "owner_id")
    op.drop_constraint("posts_users_fk", "posts")
    pass
