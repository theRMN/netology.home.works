import requests
import datetime
from pprint import pprint

request = requests.get('https://api.stackexchange.com/2.2/questions',
                       params={'fromdate': '1614643200',
                               'todate': '1614816000',
                               'order': 'desc',
                               'sort': 'week',
                               'tagged': 'python',
                               'site': 'stackoverflow'})

for i in request.json()['items']:
    print(i['link'])

