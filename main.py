import requests
import re
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID ='38cf7200648b408aa37f2d51b4a55c0b'
CLIENT_SECRET = os.environ['SPOTIFYKEY']
SPOTIFY_URI = 'https://www.example.com'

scope = "user-modify-private"

sp = spotipy.oauth2.SpotifyOAuth(CLIENT_ID,CLIENT_SECRET,SPOTIFY_URI,scope=scope)

access_token = ''
token_cached = sp.get_cached_token()

if token_cached:
    access_token = token_cached['access_token']
else:
    access_token = sp.get_access_token()
    print(sp.validate_token(access_token))
    
if access_token:
    user = spotipy.Spotify(access_token)
    print(user.current_user())
    


# valid_format = r'^\d{4}-\d{2}-\d{2}$'

# URL = 'https://www.billboard.com/charts/hot-100/2002-02-02/'
# #Using the spotify api and Billboard top 100 to create a playlist of the top 100 dongs from a time period

# #input_date = input("Enter a year, month, day in (y-mm-dd) format")

# # while not re.match(valid_format, input_date):
# #     print("wrong format")
# #     input_date = input("Enter a year, month, day in (y-mm-dd) format")

# # URL+= input_date 
# # URL+= '/'

# response = requests.get(URL)
# billboard_page = response.text
# soup = BeautifulSoup(billboard_page,'html.parser')
# parsed = soup.select(selector='li ul li h3')
# song_names = [song.getText().strip() for song in parsed]

