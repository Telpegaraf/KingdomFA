"""added absent level for mastery in character class model

Revision ID: 114d7c2c5daf
Revises: 24adcad1cdc7
Create Date: 2024-06-18 11:51:47.402365

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "114d7c2c5daf"
down_revision: Union[str, None] = "24adcad1cdc7"
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
