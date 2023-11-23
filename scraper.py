from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import soupsieve

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

scraped_data = []

browser = webdriver.Chrome("c:/Users/Arjan/Downloads/chromedriver.exe")
browser.get(START_URL)

def scrape():
    bright_star_table = soup.find("table", attrs = {"class", "wikitable"})