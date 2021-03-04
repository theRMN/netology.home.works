import requests
from datetime import datetime

number = 0
current_datetime = datetime.now().timestamp()
while True:
    number += 1
    request = requests.get('https://api.stackexchange.com/2.2/questions',
                           params={'todate': str(int(current_datetime)),
                                   'fromdate': str(int(current_datetime) - 172800),
                                   'order': 'desc',
                                   'sort': 'creation',
                                   'tagged': 'python',
                                   'site': 'stackoverflow',
                                   'pagesize': 100,
                                   'page': 1
                                   })

    for i in request.json()['items']:
        print(i['link'])
