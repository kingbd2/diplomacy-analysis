import csv
import requests
from bs4 import BeautifulSoup
from datetime import date
import time

def game_url_builder(game_name: str, game_code: str, current_year: int, current_season: str):
    backstabbr_url = 'https://www.backstabbr.com/game/'
    first_year = 1901
    
    base_url = backstabbr_url + game_name + '/' + game_code + '/'
    season_urls = [str(base_url+'****/spring'), str(base_url+'****/fall'), str(base_url+'****/winter')]
    first_url = season_urls[0].replace("****", str(first_year)) 
    
    url_list = []
    
    # Calculate number of urls to build
    number_of_years = current_year - first_year
    base_number = number_of_years*3
    if current_season=="spring":
        number_of_urls = base_number + 1
    elif current_season=="fall":
        number_of_urls = base_number + 2
    else:
        number_of_urls = base_number + 3
    years_list = []
    if number_of_years==0:
        years_list.append('1901')
    else:
        for num in range(0,number_of_years):
            year = first_year+num
            years_list.append(str(year))
    current_url_number = 1
    for i, current_year in enumerate(years_list):
        if current_url_number == number_of_urls:
            break
        year_url_list = []
        for j, item in enumerate(season_urls):
            if current_url_number == number_of_urls:
                break
            year_url_list.append(item.replace("****", str(current_year)))
            current_url_number+=1
        for url in year_url_list:
            url_list.append(url) 
    url_list.append(base_url)
    return url_list  