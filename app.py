import json, base_file
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask

"""
app = Flask(__name__)
app.secret_key = "BBS my diamonds, I don't need no light to shine"


def hello_world():
    return redirect('/create')
"""

lfm = base_file.LastFM_Data()

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
    spt.get_spotify_uri(lfm.data)

    playlist_info = json.dumps({
        'name': 'Top last.fm tracks',
        'description': 'not me doing this so that i could be employed',
        'public': False
    })

    spt.create_playlist(playlist_info)
    spt.add_songs_to_playlist()

