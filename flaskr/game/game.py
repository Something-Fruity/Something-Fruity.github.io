"""Logic and routes for our game"""
from flask import render_template, Blueprint
from flask_login import login_required, current_user


game_bp = Blueprint('game_bp', __name__, template_folder='templates')


@game_bp.route("/game", methods=["GET", "POST"])
@login_required
def game():
    """Play a game"""
    return render_template('game.html', account=current_user)
