# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy

__author__ = 'fdgogogo'

from flask import Flask

app = Flask(__name__)

app.config.from_object('backend.config.ProductionConfig')
db = SQLAlchemy(app)
