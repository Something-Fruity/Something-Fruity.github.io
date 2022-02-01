from flaskr.constants import language, language_user
from flask import redirect, render_template
from flask import Blueprint
from flask import request
from flaskr.app import S


language_bp = Blueprint('language_bp', __name__, template_folder='templates')

@language_bp.route("/language")
def lang():
    current_language = S['language']
    if current_language == 'fr':
        S['language'] = 'en'
    else:
        S['language'] = 'fr'
    print('session: ',S['language'])
    print('####end language route')
    if not 'current_url' in S:
        r = request.url_rule
        S['current_url'] = r.rule
    return redirect(S['current_url'])