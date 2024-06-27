"""initial

Revision ID: 7175884f1c16
Revises: 
Create Date: 2024-06-27 12:35:25.628074

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7175884f1c16"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "actions",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_actions_name"), "actions", ["name"], unique=True)
    op.create_table(
        "armor_groups",
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("hardness", sa.SmallInteger(), nullable=False),
        sa.Column("health", sa.SmallInteger(), nullable=False),
        sa.Column("broken_threshold", sa.SmallInteger(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "armor_specializations",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_armor_specializations_name"),
        "armor_specializations",
        ["name"],
        unique=True,
    )
    op.create_table(
        "armor_traits",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_armor_traits_name"), "armor_traits", ["name"], unique=True)
    op.create_table(
        "currencies",
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("weight", sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "damage_types",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_damage_types_name"), "damage_types", ["name"], unique=True)
    op.create_table(
        "domains",
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_domains_name"), "domains", ["name"], unique=True)
    op.create_table(
        "feat_traits",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_feat_traits_name"), "feat_traits", ["name"], unique=True)
    op.create_table(
        "gods",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("alias", sa.String(length=100), nullable=False),
        sa.Column("edict", sa.String(length=300), nullable=False),
        sa.Column("anathema", sa.String(length=300), nullable=False),
        sa.Column("areas_of_interest", sa.String(length=300), nullable=False),
        sa.Column("temples", sa.String(length=300), nullable=False),
        sa.Column("worship", sa.String(length=300), nullable=False),
        sa.Column("sacred_animal", sa.String(length=300), nullable=False),
        sa.Column("sacred_color", sa.String(length=300), nullable=False),
        sa.Column("chosen_weapon", sa.String(length=300), nullable=False),
        sa.Column("taro", sa.String(length=300), nullable=False),
        sa.Column("alignment", sa.String(length=300), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_gods_name"), "gods", ["name"], unique=True)
    op.create_table(
        "prerequisites",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_prerequisites_name"), "prerequisites", ["name"], unique=True
    )
    op.create_table(
        "races",
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "requirements",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_requirements_name"), "requirements", ["name"], unique=True)
    op.create_table(
        "skills",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_skills_name"), "skills", ["name"], unique=True)
    op.create_table(
        "slots",
        sa.Column("slot", sa.String(length=100), nullable=False),
        sa.Column("limit", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slot"),
    )
    op.create_table(
        "spell_casts",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_spell_casts_name"), "spell_casts", ["name"], unique=True)
    op.create_table(
        "spell_components",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_spell_components_name"), "spell_components", ["name"], unique=True
    )
    op.create_table(
        "spell_schools",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_spell_schools_name"), "spell_schools", ["name"], unique=True
    )
    op.create_table(
        "spell_traditions",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_spell_traditions_name"), "spell_traditions", ["name"], unique=True
    )
    op.create_table(
        "spell_traits",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_spell_traits_name"), "spell_traits", ["name"], unique=True)
    op.create_table(
        "titles",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_titles_name"), "titles", ["name"], unique=True)
    op.create_table(
        "triggers",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_triggers_name"), "triggers", ["name"], unique=True)
    op.create_table(
        "users",
        sa.Column("username", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=120), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "weapon_groups",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_weapon_groups_name"), "weapon_groups", ["name"], unique=True
    )
    op.create_table(
        "weapon_masteries",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_weapon_masteries_name"), "weapon_masteries", ["name"], unique=True
    )
    op.create_table(
        "weapon_specializations",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_weapon_specializations_name"),
        "weapon_specializations",
        ["name"],
        unique=True,
    )
    op.create_table(
        "weapon_traits",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_weapon_traits_name"), "weapon_traits", ["name"], unique=True
    )
    op.create_table(
        "worn_traits",
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_worn_traits_name"), "worn_traits", ["name"], unique=True)
    op.create_table(
        "armors",
        sa.Column("armor_group_id", sa.Integer(), nullable=False),
        sa.Column(
            "category",
            sa.Enum("UNARMED", "LIGHT", "MEDIUM", "HEAVY", name="armorcategory"),
            nullable=False,
        ),
        sa.Column("ac_bonus", sa.SmallInteger(), nullable=False),
        sa.Column("dexterity_modifier_cap", sa.SmallInteger(), nullable=True),
        sa.Column("check_penalty", sa.Boolean(), nullable=False),
        sa.Column("speed_penalty", sa.Boolean(), nullable=False),
        sa.Column("strength", sa.SmallInteger(), nullable=True),
        sa.Column("level", sa.SmallInteger(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column("currency_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["armor_group_id"],
            ["armor_groups.id"],
        ),
        sa.ForeignKeyConstraint(
            ["currency_id"],
            ["currencies.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "character_classes",
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column(
            "health_by_level",
            sa.Enum("SIX", "EIGHT", "TEN", "TWELVE", name="healthbylevel"),
            nullable=False,
        ),
        sa.Column(
            "perception_mastery",
            sa.Enum(
                "ABSENT", "TRAIN", "EXPERT", "MASTER", "LEGEND", name="masterylevels"
            ),
            nullable=False,
        ),
        sa.Column(
            "fortitude_mastery",
            sa.Enum(
                "ABSENT", "TRAIN", "EXPERT", "MASTER", "LEGEND", name="masterylevels"
            ),
            nullable=False,
        ),
        sa.Column(
            "reflex_mastery",
            sa.Enum(
                "ABSENT", "TRAIN", "EXPERT", "MASTER", "LEGEND", name="masterylevels"
            ),
            nullable=False,
        ),
        sa.Column(
            "will_mastery",
            sa.Enum(
                "ABSENT", "TRAIN", "EXPERT", "MASTER", "LEGEND", name="masterylevels"
            ),
            nullable=False,
        ),
        sa.Column(
            "unarmed_mastery",
            sa.Enum(
                "ABSENT", "TRAIN", "EXPERT", "MASTER", "LEGEND", name="masterylevels"
            ),
            nullable=False,
        ),
        sa.Column(
            "light_armor_mastery",
            sa.Enum(
                "ABSENT", "TRAIN", "EXPERT", "MASTER", "LEGEND", name="masterylevels"
            ),
            nullable=False,
        ),
        sa.Column(
            "medium_armor_mastery",
            sa.Enum(
                "ABSENT", "TRAIN", "EXPERT", "MASTER", "LEGEND", name="masterylevels"
            ),
            nullable=False,
        ),
        sa.Column(
            "heavy_armor_mastery",
            sa.Enum(
                "ABSENT", "TRAIN", "EXPERT", "MASTER", "LEGEND", name="masterylevels"
            ),
            nullable=False,
        ),
        sa.Column("spell_tradition_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["spell_tradition_id"], ["spell_traditions.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "characters",
        sa.Column("first_name", sa.String(length=100), nullable=False),
        sa.Column("last_name", sa.String(length=100), nullable=False),
        sa.Column("alias", sa.String(length=100), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("race_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["race_id"],
            ["races.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "god_domain",
        sa.Column("god_id", sa.Integer(), nullable=False),
        sa.Column("domain_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["domain_id"], ["domains.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["god_id"], ["gods.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("god_id", "domain_id", name="idx_unique_god_domain"),
    )
    op.create_table(
        "weapons",
        sa.Column("damage_type_id", sa.Integer(), nullable=False),
        sa.Column("second_damage_type_id", sa.Integer(), nullable=True),
        sa.Column("weapon_group_id", sa.Integer(), nullable=True),
        sa.Column("weapon_specialization_id", sa.Integer(), nullable=True),
        sa.Column(
            "dice",
            sa.Enum("FOUR", "SIX", "EIGHT", "TEN", "TWELVE", "TWENTY", name="dice"),
            nullable=False,
        ),
        sa.Column("dice_count", sa.SmallInteger(), nullable=False),
        sa.Column("bonus_damage", sa.SmallInteger(), nullable=True),
        sa.Column(
            "second_dice",
            sa.Enum("FOUR", "SIX", "EIGHT", "TEN", "TWELVE", "TWENTY", name="dice"),
            nullable=True,
        ),
        sa.Column("second_dice_count", sa.SmallInteger(), nullable=True),
        sa.Column("second_bonus_damage", sa.SmallInteger(), nullable=True),
        sa.Column("range", sa.SmallInteger(), nullable=True),
        sa.Column("reload", sa.SmallInteger(), nullable=True),
        sa.Column("two_hands", sa.Boolean(), nullable=False),
        sa.Column("level", sa.SmallInteger(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column("currency_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["currency_id"],
            ["currencies.id"],
        ),
        sa.ForeignKeyConstraint(
            ["damage_type_id"], ["damage_types.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["second_damage_type_id"], ["damage_types.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["weapon_group_id"],
            ["weapon_groups.id"],
        ),
        sa.ForeignKeyConstraint(
            ["weapon_specialization_id"],
            ["weapon_specializations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "worns",
        sa.Column("slot_id", sa.Integer(), nullable=False),
        sa.Column("level", sa.SmallInteger(), nullable=False),
        sa.Column("activate", sa.String(), nullable=False),
        sa.Column("effect", sa.String(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column("currency_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["currency_id"],
            ["currencies.id"],
        ),
        sa.ForeignKeyConstraint(
            ["slot_id"],
            ["slots.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "armor_specialization_association",
        sa.Column("armor_id", sa.Integer(), nullable=False),
        sa.Column("armor_specialization_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["armor_id"],
            ["armors.id"],
        ),
        sa.ForeignKeyConstraint(
            ["armor_specialization_id"],
            ["armor_specializations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "armor_id",
            "armor_specialization_id",
            name="idx_unique_armor_specialization_association",
        ),
    )
    op.create_table(
        "armor_trait_association",
        sa.Column("armor_trait_id", sa.Integer(), nullable=False),
        sa.Column("armor_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["armor_id"], ["armors.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["armor_trait_id"], ["armor_traits.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "armor_trait_id", "armor_id", name="idx_unique_armor_trait_association"
        ),
    )
    op.create_table(
        "feats",
        sa.Column("character_class_id", sa.Integer(), nullable=True),
        sa.Column("action_id", sa.Integer(), nullable=False),
        sa.Column("trigger_id", sa.Integer(), nullable=False),
        sa.Column("prerequisite_id", sa.Integer(), nullable=False),
        sa.Column("requirement_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["action_id"],
            ["actions.id"],
        ),
        sa.ForeignKeyConstraint(
            ["character_class_id"],
            ["character_classes.id"],
        ),
        sa.ForeignKeyConstraint(
            ["prerequisite_id"],
            ["prerequisites.id"],
        ),
        sa.ForeignKeyConstraint(
            ["requirement_id"],
            ["requirements.id"],
        ),
        sa.ForeignKeyConstraint(
            ["trigger_id"],
            ["triggers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "weapon_trait_association",
        sa.Column("weapon_id", sa.Integer(), nullable=False),
        sa.Column("weapon_trait_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["weapon_id"], ["weapons.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["weapon_trait_id"], ["weapon_traits.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "weapon_id", "weapon_trait_id", name="idx_unique_weapon_trait_association"
        ),
    )
    op.create_table(
        "worn_item_trait",
        sa.Column("worn_id", sa.Integer(), nullable=False),
        sa.Column("worn_trait_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["worn_id"], ["worns.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["worn_trait_id"], ["worn_traits.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "worn_id", "worn_trait_id", name="idx_unique_worn_item_trait"
        ),
    )
    op.create_table(
        "feat_trait",
        sa.Column("feat_id", sa.Integer(), nullable=False),
        sa.Column("trait_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["feat_id"], ["feats.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["trait_id"], ["feat_traits.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("feat_id", "trait_id", name="idx_unique_feat_trait"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("feat_trait")
    op.drop_table("worn_item_trait")
    op.drop_table("weapon_trait_association")
    op.drop_table("feats")
    op.drop_table("armor_trait_association")
    op.drop_table("armor_specialization_association")
    op.drop_table("worns")
    op.drop_table("weapons")
    op.drop_table("god_domain")
    op.drop_table("characters")
    op.drop_table("character_classes")
    op.drop_table("armors")
    op.drop_index(op.f("ix_worn_traits_name"), table_name="worn_traits")
    op.drop_table("worn_traits")
    op.drop_index(op.f("ix_weapon_traits_name"), table_name="weapon_traits")
    op.drop_table("weapon_traits")
    op.drop_index(
        op.f("ix_weapon_specializations_name"), table_name="weapon_specializations"
    )
    op.drop_table("weapon_specializations")
    op.drop_index(op.f("ix_weapon_masteries_name"), table_name="weapon_masteries")
    op.drop_table("weapon_masteries")
    op.drop_index(op.f("ix_weapon_groups_name"), table_name="weapon_groups")
    op.drop_table("weapon_groups")
    op.drop_table("users")
    op.drop_index(op.f("ix_triggers_name"), table_name="triggers")
    op.drop_table("triggers")
    op.drop_index(op.f("ix_titles_name"), table_name="titles")
    op.drop_table("titles")
    op.drop_index(op.f("ix_spell_traits_name"), table_name="spell_traits")
    op.drop_table("spell_traits")
    op.drop_index(op.f("ix_spell_traditions_name"), table_name="spell_traditions")
    op.drop_table("spell_traditions")
    op.drop_index(op.f("ix_spell_schools_name"), table_name="spell_schools")
    op.drop_table("spell_schools")
    op.drop_index(op.f("ix_spell_components_name"), table_name="spell_components")
    op.drop_table("spell_components")
    op.drop_index(op.f("ix_spell_casts_name"), table_name="spell_casts")
    op.drop_table("spell_casts")
    op.drop_table("slots")
    op.drop_index(op.f("ix_skills_name"), table_name="skills")
    op.drop_table("skills")
    op.drop_index(op.f("ix_requirements_name"), table_name="requirements")
    op.drop_table("requirements")
    op.drop_table("races")
    op.drop_index(op.f("ix_prerequisites_name"), table_name="prerequisites")
    op.drop_table("prerequisites")
    op.drop_index(op.f("ix_gods_name"), table_name="gods")
    op.drop_table("gods")
    op.drop_index(op.f("ix_feat_traits_name"), table_name="feat_traits")
    op.drop_table("feat_traits")
    op.drop_index(op.f("ix_domains_name"), table_name="domains")
    op.drop_table("domains")
    op.drop_index(op.f("ix_damage_types_name"), table_name="damage_types")
    op.drop_table("damage_types")
    op.drop_table("currencies")
    op.drop_index(op.f("ix_armor_traits_name"), table_name="armor_traits")
    op.drop_table("armor_traits")
    op.drop_index(
        op.f("ix_armor_specializations_name"), table_name="armor_specializations"
    )
    op.drop_table("armor_specializations")
    op.drop_table("armor_groups")
    op.drop_index(op.f("ix_actions_name"), table_name="actions")
    op.drop_table("actions")
    # ### end Alembic commands ###