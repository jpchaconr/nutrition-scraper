from math import prod
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import requests
import re

SCROLL_PAUSE_TIME = 0.2

class NotFoundError(Exception):
    """Raised when an element is not found in the html"""

    def __init__(self, message) -> None:
        super().__init__(message)

def get_product_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--log-level=3");
    browser = webdriver.Chrome(options=options, executable_path='C:/webdriver/chromedriver.exe')
    browser.get(url)

    timeout_in_seconds = 15
    WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.CLASS_NAME, 'confirm')))
    browser.find_element(By.CSS_SELECTOR, 'button.confirm').click()

    # scroll to the end
    repeats = 10
    for _ in range(repeats):
        browser.execute_script("window.scrollBy(0, 250);")
        time.sleep(SCROLL_PAUSE_TIME)

    WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.CLASS_NAME, 'v-expansion-panel-header')))
    browser.find_element(By.CSS_SELECTOR, 'button.v-expansion-panel-header').click()
    browser.execute_script("window.scrollBy(0, 250);")
    time.sleep(SCROLL_PAUSE_TIME)
    html = browser.page_source

    soup = BeautifulSoup(html, features="html.parser")
    expanded_table = soup.find('div', { "class": "layout nutritional wrap"})

    return expanded_table

    # product_detail_request = requests.get(url)
    # product_detail = BeautifulSoup(product_detail_request.text, 'html.parser')

def get_portion(product_detail):
    return product_detail.find('div', class_='product-table-container').find('div').find('div').find_all('span')[1].text

def get_nutrition(product_detail):
    prod_info = product_detail.find('div', class_='product-table-container')
    if not prod_info:
        raise NotFoundError("Info not found")
    
    table = prod_info.find_all('ul')
    lis = map(lambda x: x.find_all('li'), table[1:])
    nutri_descriptors = map(lambda x: [x[0].text, float(x[1].text.strip())], lis)
    nutri_descriptors = list(map(lambda x: x + [x[0].split(' ')[-1][1:-1]], nutri_descriptors))
    return nutri_descriptors

file = open('foods_urls.txt', 'r')
tables_files = open('tables_nutrition.html', 'w', encoding='utf-8')

url = file.readline().strip('\n')
while url != '':
    print(url)
    print('------------------------')

    try:
        table = get_product_data(url)
        tables_files.write(f'<h4>{url}</h4>\n')
        tables_files.write(str(table.prettify()))
        tables_files.write('\n')
    except:
        print('FAIL:', url)

    url = file.readline().strip('\n')

file.close()
tables_files.close()
