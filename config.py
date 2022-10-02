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
    SPOTIFY_CLIENT_ID = environ.get('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = environ.get('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_USER_ID = environ.get('SPOTIFY_USER_ID')
    SPOTIFY_REDIRECT_URI = environ.get('SPOTIFY_REDIRECT_URI')
    SPOTIFY_TOKEN = environ.get('SPOTIFY_TOKEN')

