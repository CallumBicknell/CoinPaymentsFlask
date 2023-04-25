from functools import wraps
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db
from app.models.user import User
from app.users import bp


def not_loggedin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('main.profile'))
        return f(*args, **kwargs)
    return decorated_function


@bp.route('/login', methods=["GET", "POST"])
@not_loggedin
def login():
    """Login Route"""
    if request.method != "POST":
        return 'Login'
    
    # login code goes here
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('users.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))



@bp.route('/signup', methods=["GET", "POST"])
@not_loggedin
def signup():
    """Signup Route"""
    if request.method != "POST":
        return 'Signup'
    
    username = request.form.get('username')
    password = request.form.get('password')
    password_confirmation = request.form.get('password_confirmation')

    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists', "error")
        return redirect(url_for('users.signup'))

    if password != password_confirmation:
        flash('Passwords no not match', "error")
        return redirect(url_for('users.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('users.login'))



@bp.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    """Logout Route"""
    logout_user()
    return redirect(url_for('auth.login'))

