#import packages needed for web scraping
import requests    # to get website content
from bs4 import BeautifulSoup  # to traverse the website's html
import pandas as pd # to convert the html to a dataframe
#from selenium import webdriver
#from selenium.webdriver.common.by #import By

api = 'https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v5/competitions/8/seasons/2025/standings?live=false'

results = requests.get(api)

api_data = results.json()

team_names = []

team_positions = []

for data in api_data['tables']:
    for entry in data['entries']:
        team_data = entry['overall']
        del team_data['startingPosition']
        team_name = entry['team']
        team_names.append(team_name['name'])
        team_positions.append(team_data['position']) 

table = pd.DataFrame({"Club": team_names, "Position": team_positions})

print(table)

#YNWA
