import requests
from pydantic.dataclasses import dataclass
from bs4 import BeautifulSoup
import json
from typing import List, Dict
from util.utils import get_plot_data
import os

BASE_URL : str = 'https://api.utmb.world' 
OFFESET_SEARCH : int = 20 #is a UTMB site predefined number , dont change it !
OFFESET_RACE : int = 25 #is a UTMB site predefined number , dont change it !

@dataclass
class Scraper_UTMB_Api:

    @staticmethod
    def get_races(pages : int, startDate : str, endDate : str) -> List[int] :

        URL_array_races = []
        for i in range(pages):
            req = requests.get(url = f'https://api.utmb.world/search/races-qualifiers?lang=it&dateMin={startDate}&dateMax={endDate}&offset={i*OFFESET_SEARCH}')
            try:
                for race in req.json()['races']:
                    URL_array_races.append(race['uriResults'])
            except:
                print('Something Wrong, start and end date need to be in format yyyy-mm-dd \n   or just end of searching')
        return URL_array_races
    
    @staticmethod
    def get_data_race(URL_race : str, pages : int = 13 , get_json_data : bool = True, debug : bool = True) -> Dict[str, List]:
        dict_race = {}
        for i in range(pages):
            req = requests.get(f'https://api.utmb.world/races/{URL_race}/results?lang=it&offset={i*OFFESET_RACE}&gender=')
            try:
                for runner in req.json()['results']:
                    if debug:
                        print('test runner : ', runner["runnerUri"])
                    try:
                        
                        url = f'https://utmb.world/it/runner/{runner["runnerUri"]}'
                        response = requests.get(url)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        class_name = "font-16 font-d-20 font-oxanium-bold performance_stat__hcZM_"  # class to find UTMB index number to scrape
                        element = soup.find(class_=class_name)
                        dict_race[runner['fullname']] = [ (runner['time']) , int(element.text) ]
                    
                    except Exception as e:
                        print('URL errato o runner non esistente')
            except:
                print('URL errato o gara senza risultati')

        if get_json_data:
            if len(dict_race.keys()) > 3 :

                with open(f"data{URL_race}.json", "w") as file:
                    json.dump(dict_race, file, indent=4)

        return dict_race # return a dict with key value of name_runner --> [ time in the specific race, UTMB index ]
    
    @staticmethod
    def get_plots_data_race_fromJson(Json_path : str, debug : bool = True):
    
        if debug:
            print('TEST -> ', Json_path)
        with open('./data_races/'+Json_path, "r") as file:
            data = json.load(file)

        return get_plot_data(data)
    
    @staticmethod
    def UTMB_precision(race):

        folder_path = './data_races'
        file_json = os.listdir(folder_path)
        err = []
        err_race = []
        for json_data in file_json:

            times, indexs, _, _, _, _, outlier_count =  Scraper_UTMB_Api.get_plots_data_race_fromJson(json_data)
            err.append(outlier_count/len(indexs) * 100)

            if json_data == race:
                err_race.append([outlier_count, len(times)])
        return err, err_race[0][0], err_race[0][1]