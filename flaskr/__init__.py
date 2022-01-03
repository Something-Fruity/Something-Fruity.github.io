"""Set up the app when the program is initialized"""
from flask import Flask
from flask_login import LoginManager


login_manager = LoginManager()


def create_app(config='config.DevConfig'):
    """Create and return the application using the config passed in"""
    app = Flask(__name__)
    app.config.from_object(config)

    login_manager.init_app(app)

    return app
