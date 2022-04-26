from flask import Flask
from app.routes.vaccines_route import bp as bp_vaccine


def init_app(app: Flask):
    app.register_blueprint(bp_vaccine)
