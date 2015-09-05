"""nested comment support

Revision ID: 2dd22cf14d8
Revises: 47874aaac2d
Create Date: 2015-09-05 01:15:03.445479

"""

# revision identifiers, used by Alembic.
revision = '2dd22cf14d8'
down_revision = '47874aaac2d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_comment', sa.Column('by_author', sa.Boolean(), nullable=True))
    op.add_column('blog_comment', sa.Column('replied_to_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_blog_comment_replied_to_id'), 'blog_comment', ['replied_to_id'], unique=False)
    op.create_foreign_key(None, 'blog_comment', 'blog_comment', ['replied_to_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog_comment', type_='foreignkey')
    op.drop_index(op.f('ix_blog_comment_replied_to_id'), table_name='blog_comment')
    op.drop_column('blog_comment', 'replied_to_id')
    op.drop_column('blog_comment', 'by_author')
    ### end Alembic commands ###