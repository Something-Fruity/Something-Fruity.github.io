"""Initiate the application"""

from flask import Flask, flash, redirect, render_template, g
from flask_login import LoginManager

from flaskr.labels import messages

from flaskr.models.base import Session
from flaskr.models.user import User

from flaskr.game.game import game_bp
from flaskr.auth.auth import auth_bp
from flaskr.account.account import account_bp

from flask_babel import Babel, gettext
login_manager = LoginManager()

def create_app(config='config.DevConfig'):
    """Create and return the application using the config passed in"""
    application = Flask(__name__)
    application.config.from_object(config)


    application.register_blueprint(auth_bp)
    application.register_blueprint(account_bp)
    application.register_blueprint(game_bp)

    login_manager.init_app(application)

    return application


app = create_app()
session = Session()
babel = Babel(app)


@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'fr'
    
@app.before_request
def before_request():
    print(get_locale())

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return session.query(User).get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash(messages.NOT_LOGGED_IN, 'alert-danger')
    return redirect('/login')

