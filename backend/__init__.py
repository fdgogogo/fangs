# -*- coding: utf-8 -*-
import os

from flask.ext.admin import Admin
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

__author__ = 'fdgogogo'

app = Flask(__name__)

app.config.from_object(os.getenv('FANGS_CONFIG_MODULE', 'backend.config.ProductionConfig'))
db = SQLAlchemy(app)
admin = Admin(app, name='Fangs', template_mode='bootstrap3')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from backend.blog import blog

app.register_blueprint(blog)
