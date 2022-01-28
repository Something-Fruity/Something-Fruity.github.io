from flaskr.constants import language
from flask import redirect, render_template
from flask import Blueprint
from flask import g


language_bp = Blueprint('language_bp', __name__, template_folder='templates')

@language_bp.route("/language")
def lang():    
    global language
    language='en'
    print('en language',language)
    return redirect('/login')