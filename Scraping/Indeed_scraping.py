# Importing necessary library

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import pandas as pd
import time
import re
import requests
from itertools import zip_longest
from webdriver_manager.chrome import ChromeDriverManager

# Scraping job details from the indeed.com using selenium webdriver

for pageno in range(0, 27):  # Total 27 pages found
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(
        "https://nz.indeed.com/jobs?q=data+analyst&l=New+Zealand&start=" + str(10*pageno))
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.findAll('span', {'class': 'company'}):
        company_name.append(item.get_text(strip=True))
    for item in soup.findAll('span', {'class': 'location accessible-contrast-color-location'}):
        location.append(item.get_text(strip=True))
    for item in soup.findAll("div", {'class': 'title'}):
        Job_title.append(item.get_text(strip=True))
    for item in soup.find_all(name="div", attrs={"class": "row"}):
        try:
            salaries.append(div.find('nobr').text)
        except:
            try:
                div_two = div.find(name="div", attrs={"class": "sjcl"})
                div_three = div_two.find("div")
                salaries.append(div_three.text.strip())
            except:
                salaries.append("Nothing_found")
    driver.quit()

# Converting all the details into dataframe and csv file
final = []
for item in zip_longest(Job_title, company_name, location, salaries):
    final.append(item)

df = pd.DataFrame(
    final, columns=['Names', 'Company', 'Locations', 'Salary'])

# Converting into CSV

df.to_csv("indeed.csv")
