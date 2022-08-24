"""create_first_tables

Revision ID: 634d1b687e84
Revises: 
Create Date: 2021-09-12 03:13:10.348413

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '634d1b687e84'
down_revision = None
branch_labels = None
depends_on = None


def create_project_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("age", sa.Integer, nullable=False),
    )

    op.create_table(
        "issues",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("title", sa.Text, nullable=False),
        sa.Column("createdby", sa.Text, nullable=False),
    )


def upgrade() -> None:
    create_project_table()


def downgrade() -> None:
    op.drop_table("hedgehogs")
