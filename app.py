import json, base_file

"""
app = Flask(__name__)
app.secret_key = "BBS my diamonds, I don't need no light to shine"


def hello_world():
    return redirect('/create')
"""

lfm = base_file.LastFM_Data()
toptracks = lfm.lastfm_get_data()

spt = base_file.Spotify()
spt.get_spotify_uri(toptracks)

playlist_info = json.dumps({
    'name': 'Top last.fm tracks',
    'description': 'not me doing this so that i could be employed',
    'public': False
})

spt.create_playlist(playlist_info)
spt.add_songs_to_playlist()

