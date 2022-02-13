"""Routes and logic for login, logout and registering a new user"""
from datetime import date

from flask import Blueprint
from flask import render_template, request, redirect, flash
from flask_login import logout_user, current_user, login_user

from flaskr.errors.errors import InvalidEmailError, InvalidPasswordError
from flaskr.models.base import Session
from flaskr.models.user import User

from flaskr.labels import messages
from flaskr.app import S


auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')
session = Session()


@auth_bp.route("/", methods=["GET", "POST"])
def landing():
    """Redirection from landing page"""
    if current_user.is_authenticated:
        return redirect('/account')
    return redirect('/login')


@auth_bp.route("/login", methods=["GET", "POST"])
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
            login_user(user)
            session.commit()
            return redirect('/account')

        # if the user doesn't exist or the password is incorrect
        flash(messages.INCORRECT_DETAILS, 'alert-danger')
        return render_template('login.html', S=S)

    # For GET requests
    return render_template('login.html', S=S)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user"""
    if request.method == "POST":
        new_username = request.form.get("username")
        new_password = request.form.get("password")
        new_f_name = request.form.get("f_name")
        new_surname = request.form.get("surname")
        new_email = request.form.get("email")
        new_language = request.form.get("language")

        while True:
            if new_username == '' \
                    or new_password == '' \
                    or new_f_name == '' \
                    or new_surname == '' \
                    or new_language == ''\
                    or new_email == '':
                flash(messages.ALL_FIELDS_REQUIRED, 'alert-danger')
                break

            if not request.form.get("privacy"):
                flash(messages.TERMS_AND_CONDITIONS_NOT_TICKED, 'alert-danger')
                break

            # check username is not already in use
            if session.query(User).filter_by(username=new_username).first():
                flash(messages.ACCOUNT_ALREADY_EXISTS, 'alert-danger')
                break

            # check password and confirmation are the same
            if request.form.get("password") != request.form.get("confirm_password"):
                flash(messages.NON_MATCHING_PASSWORD, 'alert-danger')
                break

            try:
                user = User(new_username, new_password,
                            new_f_name, new_surname,
                            new_email, date.today(), new_language)
                session.add(user)
                session.commit()
                user = session.query(User).get(user.id)
                login_user(user)
                session.commit()

                return redirect('/account')
            except (InvalidEmailError, InvalidPasswordError) as error:
                flash(str(error), 'alert-danger')
                break

    # For GET requests or any of the error states that broke from the loop above
    return render_template("register.html", S=S)


@auth_bp.route('/logout')
def logout():
    """Log user out"""
    logout_user()
    # Redirect user to login form
    return redirect("/login")
