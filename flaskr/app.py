
from flask import Flask, render_template, session, request, redirect, flash
from flask_mysqldb import MySQL
from flask_session import Session
from tempfile import mkdtemp


app=Flask(__name__)

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



@app.route("/")
def home():
    return redirect('/register')

@app.route('/login', methods=["GET", "POST"])
def login():
    """Login with username and password"""
    global CURRENT_USER
    # Forget any stored or cached user_ids
    session.clear()
    return render_template('auth/login.html')


@app.route('/register')
def register():
    """Register for a new account"""
    return render_template('auth/register.html')


@app.route('/logout')
def logout():
    """Log user out"""
    global CURRENT_USER
    # Clear the current user's details
    session.clear()
    # Redirect user to login form
    return redirect('auth/login')
    
@app.route('/users')
def show_users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM account''')
    rv = cur.fetchall()
    return str(rv)
    
#
#if __name__ == "__main__":
#    app.run(host='0.0.0.0', debug=True)
