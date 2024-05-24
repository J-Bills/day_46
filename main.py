import requests
import re

valid_format = r'^\d{4}-\d{2}-\d{2}$'

URL = 'https://www.billboard.com/charts/hot-100/'
#Using the spotify api and Billboard top 100 to create a playlist of the top 100 dongs from a time period

input_date = input("Enter a year, month, day in (y-mm-dd) format")
if re.match(valid_format, input_date):
    URL+= input_date 
    URL+= '/'
else:
    print("wrong format")
