from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup, Comment
import csv
import lxml

#setting up an automated google chrome browser. the webdriver points to where the chrome driver is downloaded
webdriver = "/Applications/Google/chromedriver"
driver = Chrome(webdriver)