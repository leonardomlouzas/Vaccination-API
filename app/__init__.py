from flask import Flask

from app.configs import database, migration
from app import routes
from os import getenv


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    database.init_app(app)
    migration.init_app(app)

    routes.init_app(app)

    return app
