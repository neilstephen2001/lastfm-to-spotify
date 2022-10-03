# lastfm-to-spotify
 
This web app extracts music data (i.e. top songs) from last.fm, which can then be used to generate Spotify playlists.

### Get Spotify client secrets 
- Create a Spotify developer account
- Create a new application on https://developer.spotify.com/dashboard/applications
- Make note of the Spotify client ID, client secret and redirect URL
- Create a .env file, where you store these using the variable names: SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET and SPOTIFY_REDIRECT_URI

### Get last.fm API
- Obtain from https://www.last.fm/api/accounts
- Store this in the local .env file, under the variable name: LASTFM_API

### To run:
In the terminal, set up the Flask app then run the app using:
> set FLASK_APP = app
> 
> flask run

### How it should theoretically work:
- When the application is first run, you will see the homepage where you will enter the details for the data to be extracted from last.fm

[insert screenshot here once I've done the HTML] 


- Enter the information, then click 'Submit'. The data will then be displayed.

[insert screenshot here once I've done the HTML]


- If you selected to generate 'top tracks', you will have the option to export this to a Spotify playlist
- This should take you to the Spotify login page

<img width="960" alt="image" src="https://user-images.githubusercontent.com/61570582/193545974-59ff23bd-e7c6-4cc1-b1f3-62bfe239be90.png">


- After this, you will enter a playlist name and description.

[insert screenshot here once I've done the HTML]


- A public playlist will be generated on your Spotify account, and this will also be embedded into the web page

[insert screenshot here once I've done the HTML]


### To-do:
- Do the HTML stuff
- Implement Spotify authorisation using Spotipy (for creating and modifying the playlist)
