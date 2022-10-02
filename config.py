"""Flask configuration"""

from os import environ
from pickle import TRUE

class Config:
    """Set Flask config variables"""

    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = False
    SECRET_KEY = environ.get('SECRET_KEY')


    """Spotify and last.fm APIs"""
    LASTFM_API = environ.get('LASTFM_API')
    CLIENT_ID = environ.get('CLIENT_ID')
    CLIENT_SECRET = environ.get('CLIENT_SECRET')
    USER_ID = environ.get('USER_ID')

