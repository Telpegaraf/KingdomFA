"""added nullable field for character class model

Revision ID: 9777391d9644
Revises: e9bb4e38cfb3
Create Date: 2024-06-18 11:59:54.192551

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9777391d9644"
down_revision: Union[str, None] = "e9bb4e38cfb3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "characterclasss",
        "spell_tradition_id",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "characterclasss",
        "spell_tradition_id",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    # ### end Alembic commands ###