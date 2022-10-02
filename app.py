import base_file
import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect, render_template
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


# Authorising Spotify
@app.route('/')
def login():
    auth = SpotifyOAuth(
            client_id = app.config['SPOTIFY_CLIENT_ID'],
            client_secret = app.config['SPOTIFY_CLIENT_SECRET'],
            redirect_uri = app.config['SPOTIFY_REDIRECT_URI'],
            scope = 'playlist-modify-public'
    )

    return redirect('/home')


# Should get data once parameters are entered, then redirect to the display data page
@app.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        lfm = base_file.LastFM_Data()
        lfm.api_key = app.config['LASTFM_API']

        lfm.charts = request.form['charts'].strip()
        lfm.username = request.form['last.fm username'].strip()
        lfm.type = request.form['type'].strip()
        lfm.limit = request.form['limit'].strip()
        
        return render_template('display_data.html')
    
    else:
        return render_template('home.html')

# Displays last.fm data, should show an option to create playlist
"""
@app.route('/results')
def results():
"""

# Interface for creating playlist, should return 'playlist successfully created'
"""
@app.route('/create')
def results():
"""




"""
lfm = base_file.LastFM_Data()
lfm.api_key = app.config['LASTFM_API']

lfm.charts = 'user'        # 'chart' or 'user'
lfm.username = 'stvn127'    # my username
lfm.limit = 25              # number of items to extract

lfm.type = 'album'          # 'artist', 'album' or 'track' 
                            # only use 'album' option if lfm.charts = 'user'
                            # conversion to spotify playlist only works for 'track'

lfm.lastfm_get_data()       # get data
lfm.print_data()

# get song URIs and generate playlist
if lfm.type == 'track':
    spt = base_file.Spotify()
    spt.token = app.config['SPOTIFY_TOKEN']
    spt.username = app.config['SPOTIFY_USER_ID']

    spt.get_spotify_uri(lfm.data)

    playlist_info = json.dumps({
        'name': 'Top last.fm tracks',
        'description': 'not me doing this so that i could be employed',
        'public': False
    })

    spt.create_playlist(playlist_info)
    spt.add_songs_to_playlist()
"""
