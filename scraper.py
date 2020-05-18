import config
import requests
from bs4 import BeautifulSoup
import re
import argparse
from followtype import FollowType


def data(athlete_id, follow_type):
    i = 1
    while True:
        URL = 'https://www.strava.com/athletes/{}/follows?type={}&page={}'.format(str(athlete_id),
                                                                                  follow_type, str(i))

        cookies = {'_strava4_session': config.session_id}

        page = requests.get(URL, cookies=cookies)
        soup = BeautifulSoup(page.content, 'html.parser')
        follow_list = soup.find('ul', class_='following')
        results = follow_list.findAllNext(attrs={"data-athlete-id": re.compile("\d+")})

        if len(results) == 0:
            break
        for result in results:
            avatar = result.find("div", class_="avatar")
            if avatar is not None:
                print(result['data-athlete-id'], avatar['title'])
        # print result['data-athlete-id'] , avatar['title'].encode('utf-8')
        i = i + 1


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--athleteid", help="strava athlete id", type=int, required=True)
parser.add_argument("-s", "--followtype", help="following or followers", required=True, type=FollowType.argparse,
                    choices=list(FollowType))

args = parser.parse_args()
data(args.athleteid, args.followtype)
