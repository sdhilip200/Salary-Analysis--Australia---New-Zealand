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

# Assigning empty lists for storing the records

title = []
company = []
locations = []
summary = []

# Extracting the data
driver = webdriver.Chrome(ChromeDriverManager().install())
for pageno in range(0, 100):
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(
        "https://au.indeed.com/jobs?q=data+engineer&l=Australia&start=" + str(10*pageno))
    time.sleep(1)

    summaryItems = driver.find_elements_by_xpath(
        "//a[contains(@class, 'jobtitle turnstileLink')]")
    job_links = [summaryItem.get_attribute(
        "href") for summaryItem in summaryItems]

    for job_link in job_links:
        driver.get(job_link)
        time.sleep(1)

        try:

            job_title = driver.find_element_by_xpath(
                "//*[@class='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title']").text
            title.append(job_title)

        except:

            job_title = 'None'

        try:
            company_name = driver.find_element_by_xpath(
                "//div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']").text
            company.append(company_name)

        except:
            company_name = 'None'

        try:

            location = driver.find_element_by_xpath(
                "//*[@class='jobsearch-JobMetadataHeader-iconLabel']").text
            locations.append(location)

        except:

            location = 'None'

        try:

            job_description = driver.find_element_by_xpath(
                "//*[@class='jobsearch-jobDescriptionText']").text
            summary.append(job_description)

        except:

            job_description = 'None'


driver.close()

# Converting all the details into dataframe and csv file
final = []
for item in zip_longest(title, company, locations, summary):
    final.append(item)

df4 = pd.DataFrame(
    final, columns=['Job_title', 'Company_name', 'Locations', 'Summary'])
# df.to_csv('booked.csv')

# Converting into csv file

df4.to_csv("indeed.csv")
