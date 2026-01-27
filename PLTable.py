#import packages needed for web scraping
import requests    # to get website content
from bs4 import BeautifulSoup  # to traverse the website's html
import pandas as pd # to convert the html to a dataframe
#from selenium import webdriver
#from selenium.webdriver.common.by #import By

api = 'https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v5/competitions/8/seasons/2025/standings?live=false'

team_names, team_positions = [], []

points, won, drawn, lost, played = [], [], [], [], []

try:
    results = requests.get(api)
    api_data = results.json()

    for data in api_data['tables']:
    
        for entry in data['entries']:
            team_data = entry['overall']
            del team_data['startingPosition']
            team_name = entry['team']
            team_names.append(team_name['name'])
            team_positions.append(team_data['position'])
            points.append(team_data['points'])
            played.append(team_data['played'])
            won.append(team_data['won'])
            drawn.append(team_data['drawn'])
            lost.append(team_data['lost'])

    table = pd.DataFrame({"Position": team_positions, "Club": team_names, 'Points': points, 'Played': played,
                        "Won": won, "Draws": drawn, "Lost": lost})
    table.set_index('Position', inplace=True)
    print(table)

except requests.exceptions.ConnectionError:
    print("Please check your Internet connection.")

#YNWA
