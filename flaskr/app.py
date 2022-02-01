"""Initiate the application"""

from flask import Flask, flash, redirect, g
from flask import session as S
#from flask_session import Session as Ses
from flask_login import LoginManager

from flaskr.labels import messages

from flaskr.models.base import Session
from flaskr.models.user import User

from flaskr.game.game import game_bp
from flaskr.auth.auth import auth_bp
from flaskr.account.account import account_bp
from flaskr.languages.languages import lang, language_bp

from flask_babel import Babel
from flaskr.constants import language, language_user

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
#Ses(app)
#language = ''

@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])    
    global language_user
    global language
    if not "language" in S:
        if not "ulanguage" in S:
            S['language'] = 'en'
        else:
            return S['ulanguage']
        
    
    
    def ignore(): 
        print('in get_locale() ', language)
        print('in get_locale()-> language_user', language_user)
        
        if language_user == '' and language == '':
            #language = 'en'
            return 'en'
        elif language_user != '' and language != '':
            return language
        else:
            return language_user
        '''if language == 'fr':
            language='en'
            print('fr language',language)
            return language
        if language == 'en':
            language='fr'
            print('fr language',language)
            return language'''
    print(S['language'])
    return S['language']    
       
@app.before_request
def before_request():
    global language
    print('####in before request',language)
    print(get_locale())
    get_locale()
    print('####end of before_request')

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    global language_user
    if user_id is not None:
        user = session.query(User).get(user_id)
        language_user = user.language
        S['ulanguage'] = user.language
        return session.query(User).get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash(messages.NOT_LOGGED_IN, 'alert-danger')
    return redirect('/login')

