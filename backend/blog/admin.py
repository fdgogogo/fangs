from flask.ext.admin.contrib.sqla import ModelView

from backend import admin, db
from backend.blog import models


class BlogCategoryModelView(ModelView):
    column_exclude_list = ('slug',)


class BlogPostModelView(ModelView):
    column_exclude_list = ('content', 'slug')


class BlogCommentModelView(ModelView):
    column_exclude_list = ('content',)


admin.add_view(BlogCategoryModelView(models.BlogCategory, db.session))
admin.add_view(BlogPostModelView(models.BlogPost, db.session))
admin.add_view(BlogCommentModelView(models.BlogComment, db.session))
