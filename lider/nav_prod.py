from time import sleep, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import json

import sys
sys.path.append('../')
from logger import Logger

class NotFoundError(Exception):
    """Raised when an element is not found in the html"""

    def __init__(self, message) -> None:
        super().__init__(message)

log_file = str(int(time()))
log = Logger(f'logs/{log_file}.txt')

urls_file = open('prods_urls.txt', 'r')
urls = urls_file.readlines()
urls_file.close()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options, executable_path='C:/webdriver/chromedriver.exe')

def get_product_info(browser, url):
    timeout_in_seconds = 5
    WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.TAG_NAME, 'h1')))

    html = browser.page_source
    product_detail = BeautifulSoup(html, features="html.parser")
    prod_info = product_detail.find('div',{ "class": "walmart-product-info"})

    if not prod_info:
        raise NotFoundError("Info not found")

    brand = prod_info.find('a').string.strip()
    name = prod_info.find('h1').string.strip()
    if name == None:
        raise NotFoundError('no name')

    name_size = name.split(',')

    name = name_size[0]
    return brand, name

def get_table(browser, url):
    timeout_in_seconds = 5
    try:
        WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.TAG_NAME, 'table')))
    except:
        raise NotFoundError('not table')

    html = browser.page_source

    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('table')
    tbody = table.tbody
    trs = tbody.find_all('tr')
    
    if trs[0].find('strong').string != "Porción:":
        raise NotFoundError('not table')
    
    tds = map(lambda x: x.find_all('td'), trs[2:])
    nutri_descriptors = map(
        lambda x: [x[0].text.strip().replace('\xa0', ' '), float(x[1].text)],
        tds
    )
    nutri_descriptors = list(map(lambda x: x + [x[0].split(' ')[-1][1:-1]], nutri_descriptors))
    return nutri_descriptors

info_file = open('prods_info2.txt', 'w', encoding='utf-8')

i = 8610
for url in urls[8609:]:
    print(i)
    i += 1
    print(url.strip())
    for attempt in range(2):
        try:
            browser.get(url)
            brand, name = get_product_info(browser, url)
            nutri = get_table(browser, url)
            info = {"brand": brand, "name": name, "nutrition": nutri}
            info_file.write(json.dumps(info, ensure_ascii=False) + '\n')
        except Exception as e:
            error = True
            print(f'Error ({attempt}):', url)
            if attempt == 1:
                print(e)
                log.error('UNKNOWN', f'{url} {str(e)}')
            continue
        error = False
        break

    print()
    print('--------')
    print()

info_file.close()
