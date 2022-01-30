"""The account not used for user authentication"""

from flask import render_template, request, redirect, flash
from flask import Blueprint

from flask_login import login_required, current_user

from flaskr.auth.auth import session
from flaskr.labels.messages import ACCOUNT_DELETED_SUCCESS
from flaskr.models.player import Player
from flaskr.models.game import Game
from flaskr.models.user import User


account_bp = Blueprint('account_bp', __name__, template_folder='templates')


@account_bp.route("/account", methods=["GET"])
@login_required
def account():
    """Display current user's account details, including players associated with that account"""

    # Query database for players associated with the current user's account
    players = session.query(Player).filter_by(user_id=current_user.id).all()

    # How many games has each player played?
    stats = {}
    for player in players:
        num_games = len(session.query(Game).filter_by(player_id=player.id).all())
        stats[player.name] = num_games

    return render_template('account.html', account=current_user, stats=stats)


@account_bp.route("/delete_account", methods=["POST"])
@login_required
def delete_account():
    user = session.query(User).filter_by(id=current_user.id).first()
    session.delete(user)
    session.commit()
    flash(ACCOUNT_DELETED_SUCCESS, 'alert-success')
    return redirect('/logout')
