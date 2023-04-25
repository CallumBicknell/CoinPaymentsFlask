from functools import wraps
from flask import g, redirect, url_for
from flask_login import current_user


def not_loggedin(f):
    """Makes sure no user is logged in before accessing the page"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('main.profile'))
        return f(*args, **kwargs)
    return decorated_function


# must be used with @login_required
def admin_login_required(f):
    """Checks that it is an admin user accessing the page"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.user.is_admin:
            return "you need to be admin", 401
        return f(*args, **kwargs)

