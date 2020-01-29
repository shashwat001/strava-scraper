import sys
import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.strava.com/athletes/id/follows?type=following'

cookies = {'_strava4_session': '5fv9bvqi2r7laj32egn22ac5ler6to'}

page = requests.get(URL, cookies=cookies)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll(attrs={"data-athlete-id":re.compile("\d+")})

print(results[0])