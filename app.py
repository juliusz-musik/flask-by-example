import os
from flask import Flask
from flask_migrate import Migrate

from models import db, Result

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(os.getenv("APP_SETTINGS", "config.DevelopmentConfig"))

db.init_app(app)
Migrate(app, db)


@app.route("/")
def index():
    secret_key = app.config.get("SECRET_KEY")
    return f"hello app, my secret is {secret_key}"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
