from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
# from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup, Comment
import os
import csv
import lxml
from webdriver_manager.chrome import ChromeDriverManager

#setting up an automated google chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())

#getting webpage in glassdoor
driver.get("https://www.glassdoor.co.nz/Salaries/australia-data-analyst-salary-SRCH_IL.0,9_IN16_KO10,22_IP5.htm")

#parsing the page through lxml option of beautifulsoup
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

# do page 6 - 17 when you get back to it
#get the occ header to write as filename
if soup.find("h1",{'data-test' : 'OccMedianHeader'}):
    fileName = soup.find("h1",{'data-test' : 'OccMedianHeader'}).text
else:
    fileName = "Data Analyst Salaries in Australia"
pageNum = "5"

# open a csv file for writing reviews into
pathAndFileName = os.getcwd() + "/glassDoorReviews/" + fileName + pageNum + ".csv"
# new_path = os.path.relpath('/glassDoorReviews/' + fileName, cur_path)

glassDoorReviews = open(pathAndFileName, 'w')
csvWriter = csv.writer(glassDoorReviews)

# writing the header
salaryDataHeader = ["jobTitle","companyName","meanPay","payRange"]
csvWriter.writerow(salaryDataHeader)

#getting each salary block
salaryBlocks = soup.findAll("div", {'class' : 'row align-items-center m-0 salaryRow__SalaryRowStyle__row'})
#once you've done that for initial page, scroll to next page and do again. save results into one main file

for block in salaryBlocks:
    entry = []

    jobTitle = block.find("div", {'class' : 'salaryRow__JobInfoStyle__jobTitle strong'}).find("a").text
    entry.append(jobTitle)

    companyName = block.find("div", {'class' : 'salaryRow__JobInfoStyle__employerName'}).text
    entry.append(companyName)

    meanPay = block.find("div", {'class' : 'salaryRow__JobInfoStyle__meanBasePay common__formFactorHelpers__showHH'}).find('span').text
    entry.append(meanPay)

    if block.find("div", {'class' : 'col-2 d-none d-md-block px-0 py salaryRow__SalaryRowStyle__amt'}).find("span", {'class' : 'strong'}):
        payRange = "N/A"
    else:
        payRange = block.find("div", {'class' : 'col-2 d-none d-md-block px-0 py salaryRow__SalaryRowStyle__amt'}).find("div", {'class' : 'strong'}).text
        entry.append(payRange)
    
    csvWriter.writerow(entry)

glassDoorReviews.close()
