# -*- coding: utf-8 -*-
__author__ = 'fdgogogo'

from flask import Flask

app = Flask(__name__)

app.config.from_object('backend.config.ProductionConfig')

