from flask import Flask, render_template, request, redirect, flash
from flask_login import login_required, logout_user, current_user, login_user, LoginManager

from tempfile import mkdtemp

from werkzeug.security import generate_password_hash

from flaskr.models.base import Session
from flaskr.models.user import User

from flaskr.labels import messages
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

login_manager = LoginManager()
login_manager.init_app(app)
session = Session()


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
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
        else:
            flash(messages.INCORRECT_DETAILS, 'alert-danger')
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

        user = User(new_username, new_password, new_f_name, new_surname, new_email, date.today())
        session.add(user)
        login_user(user)
        session.commit()

        return render_template("account.html", account=user)


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    return redirect('/account')


@app.route("/account", methods=["GET", "POST"])
@login_required
def home():
    return render_template('account.html', account=current_user)


@app.route('/logout')
@login_required
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
