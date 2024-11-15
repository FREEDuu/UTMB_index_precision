import requests

def get_races():

    URL_array_races = []

    for i in range(5):
        
        req = requests.get(url = f'https://api.utmb.world/search/races-qualifiers?lang=it&dateMin=2024-11-01&dateMax=2025-12-31&offset={i*20}')

        for race in req.json()['races']:

            URL_array_races.append(race['uriResults'])

    return URL_array_races