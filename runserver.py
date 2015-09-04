
from backend import app

if __name__ == '__main__':
    app.config.from_object('backend.config.DevelopmentConfig')
    app.run()
