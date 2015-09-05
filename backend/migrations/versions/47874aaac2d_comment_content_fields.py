"""comment content fields

Revision ID: 47874aaac2d
Revises: 333235974f4
Create Date: 2015-09-05 00:56:32.637593

"""

# revision identifiers, used by Alembic.
revision = '47874aaac2d'
down_revision = '333235974f4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_comment', sa.Column('author', sa.String(length=128), nullable=True))
    op.add_column('blog_comment', sa.Column('author_email', sa.String(length=128), nullable=True))
    op.add_column('blog_comment', sa.Column('content', sa.Text(), nullable=True))
    op.add_column('blog_comment', sa.Column('title', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_comment', 'title')
    op.drop_column('blog_comment', 'content')
    op.drop_column('blog_comment', 'author_email')
    op.drop_column('blog_comment', 'author')
    ### end Alembic commands ###