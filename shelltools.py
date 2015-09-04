from backend import app, db

app.config.from_object('backend.config.DevelopmentConfig')
ctx = app.test_request_context()
ctx.push()
app.preprocess_request()

