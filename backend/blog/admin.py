from flask.ext.admin.contrib.sqla import ModelView
from wtforms import TextAreaField
from wtforms.widgets import TextArea

from backend import admin, db
from backend.blog import models


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class BlogCategoryModelView(ModelView):
    column_exclude_list = ('slug',)


class BlogPostModelView(ModelView):
    column_exclude_list = ('content', 'slug')
    column_filters = ('category',)
    form_overrides = {
        'content': CKTextAreaField
    }
    create_template = 'admin/ckeditor.html'
    edit_template = 'admin/ckeditor.html'
    inline_models = [models.BlogComment, ]


class BlogCommentModelView(ModelView):
    column_exclude_list = ('content',)


admin.add_view(BlogCategoryModelView(models.BlogCategory, db.session))
admin.add_view(BlogPostModelView(models.BlogPost, db.session))
admin.add_view(BlogCommentModelView(models.BlogComment, db.session))
