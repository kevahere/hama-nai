from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options
from flask_simplemde import SimpleMDE
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager


db = SQLAlchemy()
bootstrap = Bootstrap()
simple = SimpleMDE()
photos = UploadSet('photos', IMAGES)
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

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

    from .admin import admin as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # initialising the app components
    bootstrap.init_app(app)
    db.init_app(app)
    simple.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # configure UploadSet
    configure_uploads(app, photos)

    return app