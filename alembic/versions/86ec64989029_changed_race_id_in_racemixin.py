"""changed race_id in RaceMixin

Revision ID: 86ec64989029
Revises: 5bfbeaa43394
Create Date: 2024-06-12 19:36:12.278601

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "86ec64989029"
down_revision: Union[str, None] = "5bfbeaa43394"
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
