from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    """
    creating the app instance
    :param config_name:
    :return:
    """

    app = Flask(__name__)

    # creating from config
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # initialising the app components
    bootstrap.init_app(app)
    db.init_app(app)

    return app