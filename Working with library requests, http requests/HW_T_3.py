import requests
import datetime
from pprint import pprint

number = 0
while True:
    number += 1

    request = requests.get('https://api.stackexchange.com/2.2/questions',
                           params={'todate': '1614859199',
                                   'fromdate': '1614729600',
                                   'order': 'desc',
                                   'sort': 'creation',
                                   'tagged': 'python',
                                   'site': 'stackoverflow',
                                   'pagesize': 100,
                                   'page': number
                                   })

    for i in request.json()['items']:
        print(i['link'])

