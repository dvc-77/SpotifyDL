import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

my_client_id = 'CLIENT ID'
my_client_secret = 'CLIENT SECRET'


#create api
def connect(id, secret):
    sp = spotipy.Spotify(
    auth_manager = SpotifyClientCredentials(
        client_id = my_client_id,
        client_secret = my_client_secret
        )
    )
    return sp


#fetch the playlist
def fetch_playlist_by_id(api,id):
    
    playlist_response = api.playlist(playlist_id=id)
    name = playlist_response['name']
    playlist_items = playlist_response['tracks']['items']
    return playlist_items, name





