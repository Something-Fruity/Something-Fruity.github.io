"""Controls the language displayed in the application"""
from flask import redirect, request, Blueprint

from flaskr.app import S

language_bp = Blueprint('language_bp', __name__, template_folder='templates')


@language_bp.route("/language")
def toggle_language():
    """Toggle between languages"""
    current_language = S['language']
    S['language'] = 'en' if current_language == 'fr' else 'fr'

    if 'current_url' not in S:
        req = request.url_rule
        S['current_url'] = req.rule
    return redirect(S['current_url'])
