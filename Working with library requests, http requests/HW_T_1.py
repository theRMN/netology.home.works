import requests


def parsing_iq(names=None):
    if names is None:
        names = ['Hulk', 'Captain America', 'Thanos']

    intelligence_dict = {}
    x = []

    for name in names:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + name
        resp = requests.get(url)
        intelligence = int(resp.json()['results'][0]['powerstats']['intelligence'])  # We get the IQ
        hero_name = resp.json()['results'][0]['name']  # We get the name of superhero
        intelligence_dict[hero_name] = intelligence
        x.append(intelligence)

    return {max(x): intelligence_dict}


def calculating_iq(parsing=None):
    if parsing is None:
        parsing = parsing_iq()

    for intelligence_dict in parsing.items():
        for item in intelligence_dict[1].items():
            if item[1] == intelligence_dict[0]:
                print(f'Superhero with maximum iq is: "{item[0]}"')


calculating_iq()
