from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import AdminIndexView
from flask_security import current_user
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask import abort, request, url_for, redirect
from flask_admin import helpers as admin_helpers, Admin

from backend import db, security, app
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


class AuthorizationRequiredMixin(object):
    @staticmethod
    def is_accessible():
        if not current_user.is_active() or not current_user.is_authenticated():
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated():
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class AuthorizedIndexView(AuthorizationRequiredMixin, AdminIndexView):
    pass


class AuthorizedModelView(AuthorizationRequiredMixin, ModelView):
    pass


class BlogCategoryModelView(AuthorizedModelView):
    column_exclude_list = ('slug',)
    can_view_details = True


class BlogPostModelView(AuthorizedModelView):
    column_exclude_list = ('content', 'slug')
    column_filters = ('category',)
    # form_overrides = {
    #     'content': CKTextAreaField
    # }
    create_template = 'admin/ckeditor.html'
    edit_template = 'admin/ckeditor.html'
    # inline_models = [models.BlogComment, ]
    column_searchable_list = ('title', 'content')


class BlogCommentModelView(AuthorizedModelView):
    column_exclude_list = ('content',)
    form_overrides = {
        'content': CKTextAreaField
    }
    create_template = 'admin/ckeditor.html'
    edit_template = 'admin/ckeditor.html'
    can_view_details = True


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )


admin = Admin(app,
              name='Fangs',
              template_mode='bootstrap3',
              index_view=AuthorizedIndexView())

admin.add_view(BlogCategoryModelView(models.BlogCategory, db.session))
admin.add_view(BlogPostModelView(models.BlogPost, db.session))
admin.add_view(BlogCommentModelView(models.BlogComment, db.session))
