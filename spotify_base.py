import requests
import json, get_api

class Spotify:
    def __init__(self):
        self.token = get_api.spotify_token()
        self.username = get_api.spotify_user()

        self.headers = {"Content-Type": "application/json",
                                "Authorization": f"Bearer {self.token}"}
        
        self.uri_list = []
        self.playlist_info = None
        self.playlist_id = None


    def get_spotify_uri(self, song_info):
        uri_list = []
        for item in song_info:
            url = f"https://api.spotify.com/v1/search?query=track%3A{item['name']}+artist%3A{item['artist']}&type=track&offset=0&limit=5"
            response = requests.get(url, headers=self.headers)
            res= response.json()
            
            uri = res['tracks']['items']
            if not uri:
                break
            uri_list.append(uri[0]['uri'])

        self.uri_list = uri_list


    def create_playlist(self, playlist_info):
        url = f"https://api.spotify.com/v1/users/{self.username}/playlists"
        response = requests.post(url, data=playlist_info, headers=self.headers)
        if response.status_code != 201:
            self.exceptions(response)
        else:
            res = response.json()
            self.playlist_id = res['id']
    

    def add_songs_to_playlist(self):

        url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"
        uri = json.dumps({'uris': self.uri_list})
        
        response = requests.post(url, data=uri, headers=self.headers)
        if response.status_code != 201:
            print("hi")
            self.exceptions(response)
        else:
            print("Playlist successfully created")

    
    def exceptions(self, response):
        print("Exception occurred with status code: ", response.status_code)
        print("Error: ", response.text)




