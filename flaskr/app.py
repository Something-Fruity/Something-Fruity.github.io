"""The main routes of the application"""

from datetime import date

from flask import Flask, render_template, request, redirect, flash
from flask_login import login_required, logout_user, current_user, login_user, LoginManager


from flaskr.errors.errors import InvalidEmailError, InvalidPasswordError
from flaskr.models.base import Session
from flaskr.models.user import User
from flaskr.models.player import Player
from flaskr.models.game import Game

from flaskr.labels import messages


app = Flask(__name__)
app.config.from_object('config.DevConfig')

login_manager = LoginManager()
login_manager.init_app(app)
session = Session()


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    if current_user.is_authenticated:
        return redirect('/account')

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Query database for student_id
        user = session.query(User).filter_by(username=username).first()

        if user and user.check_password(password):
            flash(f'Welcome, {user.username}.', 'alert-success')
            session.query(User).filter_by(username=username).update({'last_login': date.today()})
            session.commit()
            login_user(user)
            return redirect("/account")

        # if the user doesn't exist or the password is incorrect
        flash(messages.INCORRECT_DETAILS, 'alert-danger')
        return render_template('auth/login.html')

    # For GET requests
    return render_template('auth/login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user"""
    if request.method == "POST":
        new_username = request.form.get("username")
        new_password = request.form.get("password")
        new_f_name = request.form.get("f_name")
        new_surname = request.form.get("surname")
        new_email = request.form.get("email")

        if new_username == '' \
                or new_password == '' \
                or new_f_name == '' \
                or new_surname == '' \
                or new_email == '':
            flash(messages.ALL_FIELDS_REQUIRED, 'alert-danger')
            return render_template('auth/register.html')

        # check username is not already in use
        if session.query(User).filter_by(username=new_username).first():
            flash(messages.ACCOUNT_ALREADY_EXISTS, 'alert-danger')
            return render_template('auth/register.html')

        # check password and confirmation are same
        if request.form.get("password") != request.form.get("confirm-password"):
            flash(messages.NON_MATCHING_PASSWORD, 'alert-danger')
            return render_template('auth/register.html')

        try:
            user = User(new_username, new_password,
                        new_f_name, new_surname,
                        new_email, date.today())
        except (InvalidEmailError, InvalidPasswordError) as error:
            flash(str(error), 'alert-danger')
            return redirect('/register')

        session.add(user)
        login_user(user)
        session.commit()

        return render_template("account.html", account=user)

    # For GET requests
    return render_template("auth/register.html")


@app.route("/account", methods=["GET", "POST"])
@login_required
def home():
    """Display current user's account details, including players associated with that account"""
    # Query database for players associated with the current user's account
    players = session.query(Player).filter_by(user_id=current_user.id).all()

    # How many games has each player played?
    stats = {}
    for player in players:
        num_games = len(session.query(Game).filter_by(player_id=player.id).all())
        stats[player.name] = num_games

    return render_template('account.html', account=current_user, stats=stats)


@app.route("/game", methods=["GET", "POST"])
@login_required
def game():
    """Play a game"""
    return render_template('game.html', account=current_user)


@app.route('/logout')
def logout():
    """Log user out"""
    logout_user()
    # Redirect user to login form
    return redirect("/login")


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return session.query(User).get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash(messages.NOT_LOGGED_IN, 'alert-danger')
    return redirect('/login')
