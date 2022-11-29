from pkgutil import get_data
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import requests
import re
import time

url = "https://comoquiero.net/es-CL/search"

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options, executable_path='C:/webdriver/chromedriver.exe')
browser.get(url)
timeout_in_seconds = 10
# WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.TAG_NAME, 'table')))

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

# for _ in range(10):
#     print('scrollll')
#     browser.execute_script("window.scrollBy(0, 250);")
#     time.sleep(2)

while True:
    # Scroll down to bottom
    repeats = 5
    for _ in range(repeats):
        browser.execute_script("window.scrollBy(0, 250);")
        time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        browser.execute_script("window.scrollBy(0, -400);")
        for _ in range(repeats):
            browser.execute_script("window.scrollBy(0, 250);")
            time.sleep(SCROLL_PAUSE_TIME + 1)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

    last_height = new_height

html = browser.page_source

soup = BeautifulSoup(html, features="html.parser")
items = soup.find_all('li')
print(len(items))
