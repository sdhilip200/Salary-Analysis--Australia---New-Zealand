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

for pageno in range(1,207):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #getting webpage in glassdoor
    if pageno == 1:
        driver.get("https://www.glassdoor.co.nz/Salaries/us-data-scientist-salary-SRCH_IL.0,2_IN1_KO3,17.htm")
    else:
        driver.get(
            "https://www.glassdoor.co.nz/Salaries/us-data-scientist-salary-SRCH_IL.0,2_IN1_KO3,17" + "_IP" + str(pageno) + ".htm"
        )
    time.sleep(3)

    #parsing the page through lxml option of beautifulsoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    # #get the occ header to write as filename
    # if soup.find("h1",{'data-test' : 'OccMedianHeader'}):
    #     fileName = soup.find("h1",{'data-test' : 'OccMedianHeader'}).text
    # else:
    #     fileName = "Data Scientist Salaries United States"

    # # open a csv file for writing reviews into
    # pathAndFileName = os.getcwd() + "/glassDoorReviews/" + fileName + ".csv"
    # # new_path = os.path.relpath('/glassDoorReviews/' + fileName, cur_path)

    # glassDoorReviews = open(pathAndFileName, 'w')
    # csvWriter = csv.writer(glassDoorReviews)

    # # writing the header
    # salaryDataHeader = ["jobTitle","companyName","meanPay","payRange"]
    # csvWriter.writerow(salaryDataHeader)

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
            payRange = block.find("div", {'class' : 'col-2 d-none d-md-block px-0 py salaryRow__SalaryRowStyle__amt'}).find("span", {'class' : 'strong'}).text
            pay_range.append(payRange)
        except:
            pay_range.append("N/A")

        driver.quit()

final = []
for item in zip_longest(job_title, company_name, mean_pay, pay_range):
    final.append(item)

df = pd.DataFrame(
    final, columns=['jobTitle', 'companyName', 'meanPay', 'payRange'])

df.to_csv("Data Scientist Salaries United States.csv")

