from flask.ext.restless import APIManager
from flask.ext.security import SQLAlchemyUserDatastore, Security

from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app)
db = SQLAlchemy(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)

import backend.auth.models

user_datastore = SQLAlchemyUserDatastore(
    db,
    backend.auth.models.User,
    backend.auth.models.Role)
security = Security(app, user_datastore)

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
