import json, base_file,  get_api

"""
app = Flask(__name__)
app.secret_key = "BBS my diamonds, I don't need no light to shine"


def hello_world():
    return redirect('/create')
"""

obj1 = lastfm_base.LastFM_Data()
obj1.limit = 25
toptracks = obj1.lastfm_get_data()

toptrack = []
temp = dict()
temp['name'] = 'Forever Only'
temp['artist'] = 'Jaehyun'
toptrack.append(temp)

obj2 = spotify_base.Spotify()
obj2.get_spotify_uri(toptrack)


playlist_info = json.dumps({
    'name': 'Top tracks on last.fm',
    'description': 'not me doing this so that i could be employed',
    'public': False
})

obj2.create_playlist(playlist_info)
obj2.add_songs_to_playlist()
