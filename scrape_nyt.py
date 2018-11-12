inter import Browser
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

def scrape():
    url = "https://www.nytimes.com/search"

    articles = {}

    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    # Moving through pages
    time.sleep(2)
    browser.click_link_by_id('searchTextField')
    time.sleep(2)
    browser.find_by_id('searchTextField').type('yemen')
    time.sleep(2)