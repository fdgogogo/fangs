from flask.ext.admin import Admin

from flask.ext.restless import APIManager

from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app)
db = SQLAlchemy()

admin = Admin(app, name='Fangs', template_mode='bootstrap3')

api_manager = APIManager()
api_manager.init_app(app, flask_sqlalchemy_db=db)

import backend.blog
import backend.blog.models

blog_post_api_blueprint = api_manager.create_api(
    backend.blog.models.BlogPost,
    primary_key='slug',
    results_per_page=10,
    url_prefix='/api/v1',
    methods=['GET'])

blog_comment_api_blueprint = api_manager.create_api(
    backend.blog.models.BlogComment,
    results_per_page=10,
    url_prefix='/api/v1',
    methods=['GET', 'POST', ])

blog_category_api_blueprint = api_manager.create_api(
    backend.blog.models.BlogCategory,
    results_per_page=100,
    primary_key='slug',
    exclude_columns=['posts'],
    url_prefix='/api/v1',
    methods=['GET', ])

app.register_blueprint(blog.blog)
