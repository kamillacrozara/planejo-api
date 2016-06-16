from flask import Flask
from eve import Eve
from flask_sqlalchemy import SQLAlchemy
from config import config
from eve_sqlalchemy import SQL as _SQL
from eve_sqlalchemy.validation import ValidatorSQL

db = SQLAlchemy()


class SQL(_SQL):
    driver = db

eve = Eve(validator=ValidatorSQL, data=SQL)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # attach routes and custom error pages here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
