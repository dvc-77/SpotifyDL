import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

my_client_id = 'CLIENT ID'
my_client_secret = 'CLIENT SECRET'


#Create API
def connect(id, secret):
    sp = spotipy.Spotify(
    auth_manager = SpotifyClientCredentials(
        client_id = my_client_id,
        client_secret = my_client_secret
        )
    )
    return sp


#Fetch the playlist
def fetch_playlist_by_id(api, id):
    playlist_response = api.playlist(playlist_id=id)
    name = playlist_response['name']
    playlist_items = playlist_response['tracks']['items']
    return playlist_items, name


#Extract data from Playlist
def extract_data(api, items):
    data = []
    for i in items:
        item = dict.fromkeys(['track_name','artist_name','album_name'])
        track_name = i['track']['name']
        artist_name = i['track']['artists'][0]['name']
        album_name = i['track']['album']['name']

        item['track_name'] = track_name
        item['artist_name']= artist_name
        item['album_name']= album_name

        data.append(item)
    return data


#Build queries to search on Youtube 
def query_builder(playlist_data):
    queries = []
    for song in playlist_data:
        s = "{} {} {}".format(song['track_name'], song['album_name'], song['artist_name'])
        queries.append(s)
    return queries





