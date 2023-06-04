from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("C:/Users/Tony Chen/Downloads/chromedriver_win32")
browser.get(START_URL)

time.sleep(10)
scraped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})

    table_body = bright_star_table.find('tbody')

    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)

        temp_list = []
        
        for col_data in table_cols:
            data = col_data.text.strip()

            temp_list.append(data)
            print(data)

        scraped_data.append(temp_list)


scrape()

stars_data = []

for i in range(0, len(scraped_data)):
    star_names = scraped_data[i][0]
    distance = scraped_data[i][5]
    mass = scraped_data[i][8]
    radius = scraped_data[i][9]

    required_data = [star_names, distance, mass, radius]
    stars_data.append(required_data)

headers = ['Star_name', 'Distance', 'Mass', 'Radius']

star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")

