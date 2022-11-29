from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

url = 'https://www.lider.cl/supermercado/category/Carnes_y_Pescados/Vacuno'

options = Options()
# options.add_argument('--headless')
browser = webdriver.Chrome(service=Service('C:/webdriver/chromedriver.exe'), options=options)

prods_file = open('prods_urls.txt', 'w')

sections = open('sections_urls.txt', 'r')
sections_urls = sections.readlines()
print(sections_urls)
sections.close()

for section_url in sections_urls:
    section_url = section_url.strip()
    i = 1
    while True:
        print(i)
        url = f'{section_url}?page={i}'
        browser.get(url)
        sleep(5)
        lis = browser.find_elements("xpath", "//li[contains(@class, 'ais-Hits-item')]//a")
        for link in lis:
            prods_file.write(link.get_attribute('href') + '\n')
        try:
            next_page = browser.find_element("xpath", "//li[contains(@class, 'ais-Pagination-item--nextPage')]//a[@aria-disabled='true']")
            break
        except:
            i += 1

prods_file.close()
