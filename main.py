import requests
import re
from bs4 import BeautifulSoup

valid_format = r'^\d{4}-\d{2}-\d{2}$'

URL = 'https://www.billboard.com/charts/hot-100/2002-02-02/'
#Using the spotify api and Billboard top 100 to create a playlist of the top 100 dongs from a time period

#input_date = input("Enter a year, month, day in (y-mm-dd) format")

# while not re.match(valid_format, input_date):
#     print("wrong format")
#     input_date = input("Enter a year, month, day in (y-mm-dd) format")

# URL+= input_date 
# URL+= '/'

response = requests.get(URL)
billboard_page = response.text
soup = BeautifulSoup(billboard_page,'html.parser')
parsed = soup.select(selector='li ul li h3')
song_names = [song.getText().strip() for song in parsed]

print(song_names)

