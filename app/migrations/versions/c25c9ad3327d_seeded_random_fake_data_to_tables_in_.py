"""seeded random fake data to tables in database

Revision ID: c25c9ad3327d
Revises: b1b48fb2652a
Create Date: 2023-12-17 11:15:11.509321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c25c9ad3327d'
down_revision = 'b1b48fb2652a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookCheckouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bookID', sa.Integer(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('checkoutDate', sa.Date(), nullable=True),
    sa.Column('returnDate', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['bookID'], ['books.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookCheckouts')
    # ### end Alembic commands ###