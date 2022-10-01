import requests
import json, get_api


class LastFM_Data:
    def __init__(self):
        self.user_agent = 'stvn127'
        self.api_key = get_api.lastfm_api()
        self.data = None

        # default parameters, can be replaced with user input
        self.charts = 'user'
        self.type = 'track'
        self.limit = 25
        self.username = 'stvn127'

        # parameters needed to get last.fm data
        self.url = 'https://ws.audioscrobbler.com/2.0/'
        self.headers = {'user-agent': self.user_agent}

    def user_inputs(self):

        # Determine whether to extract top charts or user data
        self.charts = input("\nType: \t'chart' to get lastfm chart data \n\t'user' to get specific user data: ")

        # Determine whether to extract top artists, albums or tracks
        if self.charts == 'chart':
            self.type = input("\nType: \t'artist' to get top artists \n\t'track' to get top tracks: ")
            if self.type != 'artist' and self.type != 'track':
                self.type = input("Invalid input, type 'artist' or 'track': ")
        elif self.charts == 'user':
            self.username = input("\nEnter last.fm username: ")
            self.type = input(
                "\nType: \t'artist' to get top artists \n\t'album' to get top albums \n\t'track' to get top tracks: ")
            if self.type != 'artist' and self.type != 'album' and self.type != 'track':
                self.type = input("Invalid input, type 'artist', 'album' or 'track': ")
        else:
            self.charts = input("\nInvalid input, type 'chart' or 'user': ")

        # Number of items to be extracted
        while True:
            try:
                self.limit = int(input("\nEnter the number of " + self.type + "s to output: "))
                if self.limit <= 0:
                    self.limit = int(input("Enter a positive integer: "))
                break
            except ValueError:
                print("Enter a positive integer")

    def print_data(self):
        if self.charts == 'chart':
            print("\n\nTop %d %ss on the last.fm charts" % (self.limit, self.type))
        elif self.charts == 'user':
            print("\n\nTop %d %ss of user %s" % (self.limit, self.type, self.username))

        if self.type == 'artist':
            for i in range(len(self.data)):
                print("%d.\t%s" % (i + 1, self.data[i]))
        elif self.type == 'album' or self.type == 'track':
            for i in range(len(self.data)):
                print("%d.\t%s - %s" % (i + 1, self.data[i]['artist'], self.data[i]['name']))

    def get_params(self):
        params = {'limit': self.limit, 'api_key': self.api_key, 'format': 'json'}

        if self.charts == 'chart':
            if self.type == 'artist':
                params['method'] = 'chart.gettopartists'
                attr = 'artists'
            elif self.type == 'track':
                params['method'] = 'chart.gettoptracks'
                attr = 'tracks'
        elif self.charts == 'user':
            params['user'] = self.username
            if self.type == 'artist':
                params['method'] = 'user.gettopartists'
                attr = 'topartists'
            elif self.type == 'album':
                params['method'] = 'user.gettopalbums'
                attr = 'topalbums'
            elif self.type == 'track':
                params['method'] = 'user.gettoptracks'
                attr = 'toptracks'

        return params, attr

    def organise_data(self, data, attr):

        # output variable
        info = []

        if self.type == 'artist':
            for item in data[attr]['artist']:
                info.append(item['name'])
        elif self.type == 'album' or self.type == 'track':
            for item in data[attr][self.type]:
                temp = dict()
                temp['name'] = item['name']
                temp['artist'] = item['artist']['name']
                info.append(temp)

        self.data = info
        return info

    def lastfm_get_data(self):

        # get parameters for last.fm data extraction
        [params, attr] = self.get_params()

        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code != 200:
            self.exceptions(response)
        else:
            res = response.json()
            data = self.organise_data(res, attr)

        return data

    def exceptions(self, response):
        print("Exception occurred with status code: ", response.status_code)
        print("Error: ", response.text)


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