class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.sqlite3'
    DEBUG = True
    SECRET_KEY = 'xaeY\xcc\xfd\x8bS\x1d\xe8W\xe6\xc6#\xd90\xb7\xfa\xcc\x94\xc3y!*\xfe\xc0'


class TestingConfig(Config):
    TESTING = True
