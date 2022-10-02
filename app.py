import json, base_file
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


lfm = base_file.LastFM_Data()
lfm.api_key = app.config['LASTFM_API']

lfm.charts = 'user'        # 'chart' or 'user'
lfm.username = 'stvn127'    # my username
lfm.limit = 25              # number of items to extract

lfm.type = 'track'          # 'artist', 'album' or 'track' 
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

