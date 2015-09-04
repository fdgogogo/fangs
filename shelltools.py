from backend import app, db

from backend.blog.models import BlogCategory, BlogPost, BlogComment

app.config.from_object('backend.config.DevelopmentConfig')
ctx = app.test_request_context()
ctx.push()
app.preprocess_request()

