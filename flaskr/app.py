"""Initiate the application"""

from flask import Flask, flash, redirect
from flask import session as S

from flask_login import LoginManager
from flask_babel import Babel

from flaskr.labels import messages

from flaskr.models.base import Session
from flaskr.models.user import User

from flaskr.game.game import game_bp
from flaskr.auth.auth import auth_bp
from flaskr.account.account import account_bp
from flaskr.languages.languages import language_bp


login_manager = LoginManager()


def create_app(config='config.DevConfig'):
    """Create and return the application using the config passed in"""
    application = Flask(__name__)
    application.config.from_object(config)

    application.register_blueprint(auth_bp)
    application.register_blueprint(account_bp)
    application.register_blueprint(game_bp)
    application.register_blueprint(language_bp)

    login_manager.init_app(application)

    return application


app = create_app()
session = Session()
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns the locale selected by the user"""
    if "language" not in S:
        if "ulanguage" not in S:
            S['language'] = 'en'
        else:
            return S['ulanguage']
    return S['language']


@app.before_request
def before_request():
    """Ensure locale is checked before every request"""
    get_locale()


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        user = session.query(User).get(user_id)
        S['ulanguage'] = user.language
        return session.query(User).get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash(messages.NOT_LOGGED_IN, 'alert-danger')
    return redirect('/login')
