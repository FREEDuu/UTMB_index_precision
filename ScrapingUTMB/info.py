import requests
from bs4 import BeautifulSoup
import json
from API_scrape_races import get_races


URL_races = get_races()

for race in URL_races:
    
    res_dict = {}

    for i in range(13):
        
        req = requests.get(f'https://api.utmb.world/races/{race}/results?lang=it&offset={i*25}&gender=')

        print('test GARA --> ' , race)

        try:

            for runner in req.json()['results']:

                try:

                    url = f'https://utmb.world/it/runner/{runner["runnerUri"]}'
                    response = requests.get(url)

                    soup = BeautifulSoup(response.text, 'html.parser')

                    class_name = "font-16 font-d-20 font-oxanium-bold performance_stat__hcZM_"  # Replace with the class name you want to search
                    element = soup.find(class_=class_name)
                    res_dict[runner['fullname']] = [runner['time'], element.text]
                
                except:

                    print('RUNNER SENZA RISULTATI')
            
        except:

            print('GARA SENZA RISULTATI')

    if len(res_dict.keys()) > 3 :

        with open(f"data{race}.json", "w") as file:
            json.dump(res_dict, file, indent=4)

