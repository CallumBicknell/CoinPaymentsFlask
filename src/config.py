import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Class to contain all of the apps confirguration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Caching related configs
    CACHE_TYPE = "SimpleCache" 
    CACHE_DEFAULT_TIMEOUT = 300
