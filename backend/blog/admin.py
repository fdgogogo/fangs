from flask.ext.admin.contrib.sqla import ModelView
from backend import admin, db

from backend.blog import models

admin.add_view(ModelView(models.BlogCategory, db.session))
admin.add_view(ModelView(models.BlogPost, db.session))
admin.add_view(ModelView(models.BlogComment, db.session))
