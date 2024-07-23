"""changed unique for armor groups

Revision ID: 59b5ba33eda2
Revises: 8956c42454ad
Create Date: 2024-07-23 12:57:04.451099

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "59b5ba33eda2"
down_revision: Union[str, None] = "8956c42454ad"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "armor_groups", ["name"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "armor_groups", type_="unique")
    # ### end Alembic commands ###
