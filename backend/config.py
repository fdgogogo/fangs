SQLALCHEMY_DATABASE_URI = 'postgresql://'
DEBUG = True
SECRET_KEY = 'xaeY\xcc\xfd\x8bS\x1d\xe8W\xe6\xc6#\xd90\xb7\xfa\xcc\x94\xc3y!*\xfe\xc0'
STATIC_FOLDER = 'static'

try:
    # create `backend/local_config.py` to override configs
    from backend.local_config import *
except ImportError:
    pass
