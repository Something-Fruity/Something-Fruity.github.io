
from flask import Flask, render_template, session, request, redirect, flash
from flask_mysqldb import MySQL
from flask_session import Session
from tempfile import mkdtemp

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.classes import Account
from flaskr.helper import apology
from flaskr.database_helper import db_select, db_commit


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem instead of cookies
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_HOST"] = "172.19.0.2"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_DB"] = "sth_fruity"
mysql = MySQL(app)
Session(app)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username and password:
            return apology("incomplete details", 403)

        # Query database for student_id
        cmd = "SELECT * FROM account WHERE username =%s"
        results = db_select(mysql, cmd, [username])

        if len(results) != 1:
            return apology("invalid details", 403)

        account = Account(results[0])
        if check_password_hash(password, account.hash):
            return apology("incorrect password", 403)

        # Remember which user has logged in
        session["account_id"] = account.id

        return render_template("account.html", account=account)

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
            return apology('must complete all fields', 403)

        new_account = Account(new_username, new_password, new_f_name, new_surname, new_email)

        # check password and confirmation are same
        if request.form.get("password") != request.form.get("confirm-password"):
            return apology("password and confirmation do not match", 403)

        # check username is unique
        if db_select(mysql, "SELECT * FROM account WHERE username = %s", [new_username]):
            return apology("you already have an account", 403)

        # create row in db
        db_commit(mysql, "INSERT INTO account(username, hash, f_name, surname, email) VALUES (%s, %s, %s, %s, %s)",
                  new_account.get_details())

        # make sure that the new user is logged in
        results = db_select(mysql, "SELECT * FROM account WHERE username = %s", [new_account.username])

        # # set the session, so we know who is logged-in
        session["account_id"] = results[0][0]
        return render_template("account.html", account=new_account)


@app.route("/", methods=["GET", "POST"])
@app.route("/account", methods=["GET", "POST"])
def home(account):
    if request.method == "GET":
        return render_template('account.html', account=account)


@app.route('/logout')
def logout():
    """Log user out"""
    # Clear the current user's details
    session.clear()
    # Redirect user to login form
    return redirect("/login")



    
@app.route('/users')
def show_users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM account''')
    rv = cur.fetchall()
    return str(rv)

