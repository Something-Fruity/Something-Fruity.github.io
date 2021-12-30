from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from flask_session import Session
from tempfile import mkdtemp

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.models.base import Session
from flaskr.models.account import Account
from flaskr.models.player import Player
from flaskr.models.persona import Persona
from flaskr.models.game import Game

from datetime import date

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem instead of cookies
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_DB"] = "sth_fruity"

app.secret_key = 'super secret key'

session = Session()


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Query database for student_id
        account = session.query(Account).filter_by(username=username).first()

        if account and account.check_password(password):
            flash(f'Welcome, {account.username}.', 'alert-success')
            session.query(Account).filter_by(username=username).update({'last_login': date.today()})
            session.commit()
            return render_template("account.html", account=account)
        else:
            flash("INCORRECT DETAILS: Please check your details and try again.", 'alert-danger')
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        # Display form for user to create account
        return render_template("auth/register.html")
    else:
        new_username = request.form.get("username")
        new_password = generate_password_hash(request.form.get("password"))
        new_f_name = request.form.get("f_name")
        new_surname = request.form.get("surname")
        new_email = request.form.get("email")

        if new_username == '' or new_password == '' or new_f_name == '' or new_surname == '' or new_email == '':
            flash("You must complete all fields", 'alert-danger')
            return render_template('auth/register.html')

        # check username is unique
        if session.query(Account).filter_by(username=new_username).first():
            flash("There is already an account associated with this username", 'alert-danger')
            return render_template('auth/register.html')

        # check password and confirmation are same
        if request.form.get("password") != request.form.get("confirm-password"):
            flash("Your password and confirmation do not match", 'alert-danger')
            return render_template('auth/register.html')

        new_account = Account(new_username, new_password, new_f_name, new_surname, new_email, date.today())
        session.add(new_account)
        session.commit()

        # # make sure that the new user is logged in
        return render_template("account.html", account=new_account)


@app.route("/", methods=["GET", "POST"])
def index():
    return redirect('/account')


@app.route("/account", methods=["GET", "POST"])
def home():
    return render_template('account.html', account=None)


@app.route('/logout')
def logout():
    """Log user out"""
    # Clear the current user's details
    session.clear()
    # Redirect user to login form
    return redirect("/login")



