import base_file
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect, render_template
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def test():
    auth = SpotifyOAuth(
            client_id = app.config['SPOTIFY_CLIENT_ID'],
            client_secret = app.config['SPOTIFY_CLIENT_SECRET'],
            redirect_uri = app.config['SPOTIFY_REDIRECT_URI'],
            scope = 'user-read-recently-played'
    )

    sp = spotipy.Spotify(auth_manager = auth)

    results = sp.current_user_recently_played()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx+1, track['artists'][0]['name'], " – ", track['name'])
    
    return render_template('home.html')

@app.route('/home')
def home():
    lfm = base_file.LastFM_Data()
    lfm.api_key = app.config['LASTFM_API']

    lfm.charts = request.form['charts']
    lfm.username = request.form['last.fm username']
    lfm.type = request.form['type']
    lfm.limit = request.form['limit']

    return render_template('display_data.html')

if __name__ == "__main__":
    app.run()



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
