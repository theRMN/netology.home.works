import requests
from datetime import datetime


def datetime_now():
    current_datetime = datetime.now().timestamp()

    return current_datetime


def questions_parsing(current_datetime=None):
    if current_datetime is None:
        current_datetime = datetime_now()

    number = 0

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
                                       'page': number
                                       })

        for i in request.json()['items']:
            print(i['link'])


questions_parsing()
