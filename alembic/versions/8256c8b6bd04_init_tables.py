"""init tables

Revision ID: 8256c8b6bd04
Revises: 
Create Date: 2021-08-10 11:47:51.428377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8256c8b6bd04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "model",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column("department", sa.VARCHAR(255), nullable=False, comment=""),
        sa.Column("name", sa.VARCHAR(255), nullable=False, comment=""),
        sa.Column("path", sa.VARCHAR(255), nullable=False, comment=""),
        sa.Column("type", sa.VARCHAR(255), nullable=False, comment=""),
        sqlite_autoincrement=True,
    )


def downgrade():
    op.execute("DELETE from model")
