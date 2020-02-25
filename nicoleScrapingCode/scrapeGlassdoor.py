"""
in this script, we scrape salary data from glassdoor. Must have a glassdoor account and be logged in. 
There are a few steps you have to do manually for each scraping job. Steps are below:

Firstly, search up any job in the glassdoor *salaries* section you'd want to know salary info about

1.) Once the search is fulfilled, copy and paste the resulting URL from your browser (should be of the 1st page of salaries) to the 2x driver.get(url) links below
2.) Find out how many pages of salaries there are for that job. To do this: modify the url by adding this exact phrase: '_IP1000'. 
Navigate to that URL with your browser.
3.) In 2.), we've gone to page 1000 of the salaries page. Most jobs don't have salary info spanning 1000 pages, and so putting in that URL would direct you to the very last page 
of salary info. Find out what that page# is, by looking at the button carousel somewhere in the page
4.) Add +1 to the last page, and enter that number into the pageno range in the for loop
5.) Then modify the filename to save it as in line 90
5.) The for loop in 4.) loops through all pages of salary info for that job and scrapes data accordingly

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
# from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup, Comment
import time
import os
import csv
import lxml
from itertools import zip_longest
from webdriver_manager.chrome import ChromeDriverManager

#setting up an automated google chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())

job_title = []
company_name = []
mean_pay = []
pay_range = []

for pageno in range(1,184):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #getting webpage in glassdoor
    if pageno == 1:
        driver.get("https://www.glassdoor.co.nz/Salaries/us-data-engineer-salary-SRCH_IL.0,2_IN1_KO3,16.htm")
    else:
        driver.get(
            "https://www.glassdoor.co.nz/Salaries/us-data-engineer-salary-SRCH_IL.0,2_IN1_KO3,16.htm" + "_IP" + str(pageno) + ".htm"
        )
    time.sleep(1.5)

    #parsing the page through lxml option of beautifulsoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    #getting each salary block
    salaryBlocks = soup.findAll("div", {'class' : 'row align-items-center m-0 salaryRow__SalaryRowStyle__row'})
    #once you've done that for initial page, scroll to next page and do again. save results into one main file

    for block in salaryBlocks:
        entry = []

        jobTitle = block.find("div", {'class' : 'salaryRow__JobInfoStyle__jobTitle strong'}).find("a").text
        job_title.append(jobTitle)

        companyName = block.find("div", {'class' : 'salaryRow__JobInfoStyle__employerName'}).text
        company_name.append(companyName)

        meanPay = block.find("div", {'class' : 'salaryRow__JobInfoStyle__meanBasePay common__formFactorHelpers__showHH'}).find('span').text
        mean_pay.append(meanPay)
        
        try:
            if block.find("div", {'class' : 'col-2 d-none d-md-block px-0 py salaryRow__SalaryRowStyle__amt'}).find("div", {'class' : 'strong'}):
                payRange = block.find("div", {'class' : 'col-2 d-none d-md-block px-0 py salaryRow__SalaryRowStyle__amt'}).find("div", {'class' : 'strong'}).text
                pay_range.append(payRange)
            elif block.find("div", {'class' : 'col-2 d-none d-md-block px-0 py salaryRow__SalaryRowStyle__amt'}).find("span", {'class' : 'strong'}):
                pay_range.append("N/A")
        except:
            pay_range.append("N/A")

        driver.quit()

final = []
for item in zip_longest(job_title, company_name, mean_pay, pay_range):
    final.append(item)

df = pd.DataFrame(
    final, columns=['jobTitle', 'companyName', 'meanPay', 'payRange'])

df.to_csv("Data Engineer Salaries United States.csv")

