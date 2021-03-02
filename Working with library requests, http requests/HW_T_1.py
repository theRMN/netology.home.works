from pprint import pprint
import requests
import json

name_list = ['Hulk', 'Captain America', 'Thanos']

intelligence_dict = {}

for name in name_list:
    url = 'https://superheroapi.com/api/2619421814940190/search/' + name
    resp = requests.get(url)
    x = resp.json()
    intelligence = x['results'][0]['powerstats']['intelligence']  # Получаем показатель интелекта
    hero_name = x['results'][0]['name']
    intelligence_dict[hero_name] = intelligence

print(intelligence_dict)

# print(resp.status_code)
# print(resp.content)
# pprint(resp.headers)
# print(resp.text)
# pprint(resp.json())
