"""The account not used for user authentication"""

from flask import render_template, request
from flask import Blueprint

from flask_login import login_required, current_user

from flaskr.auth.auth import session
from flaskr.models.player import Player
from flaskr.models.game import Game
from flaskr.app import S



account_bp = Blueprint('account_bp', __name__, template_folder='templates')


@account_bp.route("/account", methods=["GET", "POST"])
@login_required
def home():
    """Display current user's account details, including players associated with that account"""
    # Query database for players associated with the current user's account
    players = session.query(Player).filter_by(user_id=current_user.id).all()
    S['current_url'] = request.url_rule.rule
    # How many games has each player played?
    stats = {}
    for player in players:
        num_games = len(session.query(Game).filter_by(player_id=player.id).all())
        stats[player.name] = num_games
    return render_template('account.html', account=current_user, stats=stats, S=S)
