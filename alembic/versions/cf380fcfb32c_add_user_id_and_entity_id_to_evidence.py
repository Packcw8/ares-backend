"""add user_id and entity_id to evidence

Revision ID: cf380fcfb32c
Revises: c46cbd783a64
Create Date: 2025-06-21 17:37:08.670455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf380fcfb32c'
down_revision: Union[str, None] = 'c46cbd783a64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('evidence', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('evidence', sa.Column('entity_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'evidence', 'rated_entities', ['entity_id'], ['id'])
    op.create_foreign_key(None, 'evidence', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'evidence', type_='foreignkey')
    op.drop_constraint(None, 'evidence', type_='foreignkey')
    op.drop_column('evidence', 'entity_id')
    op.drop_column('evidence', 'user_id')
    # ### end Alembic commands ###
