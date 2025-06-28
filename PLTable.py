#import packages needed for web scraping
import requests    # to get website content
from bs4 import BeautifulSoup  # to traverse the website's html
import pandas as pd # to convert the html to a dataframe

url = 'https://www.premierleague.com/'
try:
    page = requests.get(url)
except Exception as err:
    print(err)

else:
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('div', {'class': 'tablesContainer'})
    rows = table.find_all('tr')
finally:
    df = pd.read_html(str(table))[0]
    df.set_index("Pos", inplace=True)
    
    print(df)


#YNWA
