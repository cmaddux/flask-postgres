"""create users table

Revision ID: a331776a1a44
Revises:
Create Date: 2019-10-23 23:38:29.628414

"""
#pylint: disable=import-error
from alembic import op
import sqlalchemy as sa
#pylint: enable=import-error

# revision identifiers, used by Alembic.
revision = 'a331776a1a44'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(255), nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.sql.func.now()
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            onupdate=sa.sql.func.now()
        )
    )

def downgrade():
    op.drop_table('users')
