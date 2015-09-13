from flask.ext.admin import Admin
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.restless import APIManager
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, url_for
from flask.ext.cors import CORS

from backend.utils.wordpress_importer import ImportWordpress

app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app)
db = SQLAlchemy(app)
admin = Admin(app, name='Fangs', template_mode='bootstrap3')

api_manager = APIManager(app, flask_sqlalchemy_db=db)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.add_command('import_wordpress', ImportWordpress)

from backend.blog import blog
from backend.blog.models import BlogComment, BlogCategory, BlogPost

def post_get_many(*args, **kwargs):
    print(args)
    print(kwargs)

blog_post_api_blueprint = api_manager.create_api(
    BlogPost,
    primary_key='slug',
    results_per_page=10,
    url_prefix='/api/v1',
    methods=['GET'])

blog_comment_api_blueprint = api_manager.create_api(
    BlogComment,
    results_per_page=10,
    url_prefix='/api/v1',
    methods=['GET', 'POST', ])

blog_category_api_blueprint = api_manager.create_api(
    BlogCategory,
    results_per_page=100,
    primary_key='slug',
    exclude_columns=['posts'],
    url_prefix='/api/v1',
    methods=['GET', ])

app.register_blueprint(blog)


@manager.command
def list_routes():
    import urllib.parse
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote(
            "{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)
