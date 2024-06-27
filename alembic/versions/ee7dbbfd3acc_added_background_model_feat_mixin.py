"""added background model, feat mixin

Revision ID: ee7dbbfd3acc
Revises: c67dcb099473
Create Date: 2024-06-27 13:40:26.610541

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ee7dbbfd3acc"
down_revision: Union[str, None] = "c67dcb099473"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "backgrounds",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=200), nullable=False),
        sa.Column("feat_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["feat_id"], ["feats.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.drop_constraint("feats_character_class_id_fkey", "feats", type_="foreignkey")
    op.create_foreign_key(
        None,
        "feats",
        "character_classes",
        ["character_class_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "feats", type_="foreignkey")
    op.create_foreign_key(
        "feats_character_class_id_fkey",
        "feats",
        "character_classes",
        ["character_class_id"],
        ["id"],
    )
    op.drop_table("backgrounds")
    # ### end Alembic commands ###
