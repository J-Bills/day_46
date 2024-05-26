import requests
import re
import spotipy
from time import sleep
import os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


CLIENT_ID ='38cf7200648b408aa37f2d51b4a55c0b'
CLIENT_SECRET = os.environ['SPOTIFYKEY']
SPOTIFY_URI = 'https://www.example.com'
scope = "user-modify-private"

#Using the spotify api and Billboard top 100 to create a playlist of the top 100 dongs from a time period

valid_format = r'^\d{4}-\d{2}-\d{2}$'
URL = 'https://www.billboard.com/charts/hot-100/'


input_date = input("Enter a year, month, day in (y-mm-dd) format")

while not re.match(valid_format, input_date):
    print("wrong format")
    input_date = input("Enter a year, month, day in (y-mm-dd) format")

URL+= input_date 
URL+= '/'

def is_digit(input:str):
    return input.isdigit()

def contains_featuring(input:str):
    if 'Featuring' in input:
        start_index = input.index('Featuring')
        return input[:start_index]
    else:
        return input

response = requests.get(URL)
billboard_page = response.text
soup = BeautifulSoup(billboard_page,'html.parser')
song_title_html = soup.select(selector='div li ul li h3')
artist_html = soup.select(selector='div li ul li span',)
song_names = [song.getText().strip() for song in song_title_html]
artist_names = [contains_featuring(artist.getText().strip()) for artist in artist_html]
artist_names = [artist for artist in artist_names if is_digit(artist) == False and len(artist) > 1]


songs_and_artist = dict(zip(song_names,artist_names))


sp = spotipy.oauth2.SpotifyOAuth(CLIENT_ID,CLIENT_SECRET,SPOTIFY_URI,scope=scope)

access_token = ''
token_cached = sp.get_cached_token()



if token_cached:
    access_token = token_cached['access_token']
    #print('token acquired')
else:
    access_token = sp.get_access_token()
    #print('token acquired')
    
    
if access_token:
    user = spotipy.Spotify(access_token)
    user_id = user.current_user().get('id')
    print(user_id)
    
    track_collection_ids = list()
    for key, val in songs_and_artist.items():
        query_string = f"track:{key} artist:{val}"    
        response = user.search(q=query_string, limit=1, offset=0, type='track', market='ES')
        try:
            track_collection_ids.append(response['tracks']['items'][0]['uri'])
        except IndexError:
            pass
    
    first_half = track_collection_ids[:50]
    second_half = track_collection_ids[50:len(track_collection_ids)]
    
    playlist = user.user_playlist_create(user_id,f"{input_date} Billboard 100")
    

    user.playlist_add_items(playlist.get('id'),first_half)
    sleep(30)
    user.playlist_add_items(playlist.get('id'),second_half)
    
    print(user.playlist_items(playlist.get('id')))


