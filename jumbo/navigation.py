from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sections = [
    'https://www.jumbo.cl/lacteos', 
    'https://www.jumbo.cl/despensa', 
    'https://www.jumbo.cl/frutas-y-verduras', 
    'https://www.jumbo.cl/carniceria', 
    'https://www.jumbo.cl/bebidas-aguas-y-jugos'
]

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(service=Service('C:/webdriver/chromedriver.exe'), options=options)

browser.get(sections[0])
timeout_in_seconds = 10
WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'ul.shelf-list')))
next_page_btn = browser.find_element(By.CLASS_NAME, 'slider-next-button')
html = browser.page_source
soup = BeautifulSoup(html, features="html.parser")

## next page button
next_page = soup.find_all('button', class_='slider-next-button')
span = soup.find('span', class_='select-page-title').text
pages = span.split(' ')[1::2]
print(span.split(' ')[1::2])
print(int(pages[0]) + 1)

print(next_page)

links = list(map(lambda x: x.find('a', class_='shelf-product-title')['href'], soup.find_all('li', class_='shelf-item')))
print(links)
