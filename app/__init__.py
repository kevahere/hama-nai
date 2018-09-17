from flask import Flask
from config import config_options,Config

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()



def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)
    # Initializing flask extensions
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app