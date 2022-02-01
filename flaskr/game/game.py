"""Logic and routes for our game"""
from flask import render_template, Blueprint, request
from flask_login import login_required, current_user
from flaskr.app import S


game_bp = Blueprint('game_bp', __name__, template_folder='templates')


@game_bp.route("/game", methods=["GET", "POST"])
@login_required
def game():
    """Play a game"""
    S['current_url'] = request.url_rule.rule
    return render_template('game.html', account=current_user, S=S)
