"""added EmailStr in User

Revision ID: e38af40aa646
Revises: 554bdeaf1fe0
Create Date: 2024-06-14 18:25:24.589346

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e38af40aa646"
down_revision: Union[str, None] = "554bdeaf1fe0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("email", sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "email")
    # ### end Alembic commands ###