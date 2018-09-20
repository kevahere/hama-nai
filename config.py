import os


class Config:
    """
    class that defines the app settings
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQL_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/event_pics'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    """
    class that defines the settings when in development
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True

class ProdConfig(Config):
    """
    class that defines the settings for the deployed app
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    """
    class that defines the config for the various tests
    """
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}