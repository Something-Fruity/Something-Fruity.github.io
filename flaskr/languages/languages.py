from flaskr.constants import language, language_user
from flask import redirect, render_template
from flask import Blueprint
from flask import request
from flaskr.app import S


language_bp = Blueprint('language_bp', __name__, template_folder='templates')

@language_bp.route("/language")
def lang():
    global language_user    
    global language
    print('####language route')
    language='fr'
    S['language'] = 'fr'
    print('session: ',S['language'])
    print('####end language route')
    return redirect('/account')