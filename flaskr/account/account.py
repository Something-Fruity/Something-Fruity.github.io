"""The account not used for user authentication"""

from flask import render_template, request, redirect, flash
from flask import Blueprint

from flask_login import login_required, current_user

from flaskr.auth.auth import session
from flaskr.labels.messages import ACCOUNT_DELETED_SUCCESS, ACCOUNT_UPDATED_SUCCESS, NO_CHANGES_SAVED
from flaskr.models.player import Player
from flaskr.models.game import Game
from flaskr.models.user import User

from flaskr.helpers.helpers import is_valid_email
from flaskr.errors.errors import InvalidEmailError


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


@account_bp.route("/edit_account", methods=["GET", "POST"])
@login_required
def edit_account():
    if request.method == "GET":
        return render_template('edit_account.html', account=current_user)

    button_clicked = request.form.get('submit')
    if button_clicked == 'update':
        new_username = request.form.get("username")
        new_f_name = request.form.get("f_name")
        new_surname = request.form.get("surname")
        new_email = request.form.get("email")

        if new_username == '' or new_f_name == '' or new_surname == '' or new_email == '':
            flash(messages.ALL_FIELDS_REQUIRED, 'alert-danger')
            return render_template('edit_account.html', account=current_user)

        try:
            current_user.username = new_username
            current_user.f_name = new_f_name
            current_user.surname = new_surname
            current_user.email = is_valid_email(new_email)

            session.commit()
            flash(ACCOUNT_UPDATED_SUCCESS, 'alert-success')
            return redirect('/account')
        except InvalidEmailError as error:
            flash(str(error), 'alert-danger')
            return render_template('edit_account.html', account=current_user)

    else:
        # cancel was clicked
        flash(NO_CHANGES_SAVED, 'alert-success')
        return redirect('/account')
