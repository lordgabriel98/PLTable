#import packages needed for web scraping
import requests    # to get website content
from bs4 import BeautifulSoup  # to traverse the website's html
import pandas as pd # to convert the html to a dataframe

url = 'https://www.premierleague.com/'
try:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('div', {'class': 'tablesContainer'})
    
    if(table):
        rows = table.find_all('tr')
        df = pd.read_html(str(table))[0]
        df.set_index("Pos", inplace=True)
        print(df)
    else:
        print("Resource could not be scraped from website.")
        
except requests.exceptions.RequestException as e:
    print("Request error: ", e)


#YNWA
