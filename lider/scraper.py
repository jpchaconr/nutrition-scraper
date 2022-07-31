from pkgutil import get_data
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import requests
import re

class NotFoundError(Exception):
    """Raised when an element is not found in the html"""

    def __init__(self, message) -> None:
        super().__init__(message)

def get_product_data(url):
    product_detail_request = requests.get(url)
    product_detail = BeautifulSoup(product_detail_request.text, 'html.parser')
    prod_info = product_detail.find('h1')
    if not prod_info:
        raise NotFoundError("Info not found")

    prod_info = prod_info.find_all('span')
    brand = prod_info[0].string.strip()
    name = prod_info[1].string.strip()
    size = prod_info[2].string.strip()
    if name == None:
        raise NotFoundError('no name')

    try:
        nutrition_table = get_nutrition_html(product_detail)
        return name, size, brand, nutrition_table
    except NotFoundError as e:
        pass
    
    nutrition_table = get_nutrition_js(url)
    return name, size, brand, nutrition_table

def get_nutrition_html(parsed_html):
    table = parsed_html.find("table", class_='nutrition-table')
    if not table:
        raise NotFoundError('Table not found')

    thead = table.thead
    reference_size = thead.find_all('th')[1].string
    tbody = table.tbody.tbody
    trs = tbody.find_all('tr')
    nutri_descriptors = map(lambda x: [x.find_all('td')[0].string, float(x.find_all('td')[1].string)], trs)
    nutri_descriptors = list(map(lambda x: x + [x[0].split(' ')[-1][1:-1]], nutri_descriptors))
    return nutri_descriptors

def get_nutrition_js(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options, executable_path='C:/webdriver/chromedriver.exe')
    browser.get(url)
    timeout_in_seconds = 10
    WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.TAG_NAME, 'table')))
    html = browser.page_source

    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('table')
    tbody = table.tbody
    trs = tbody.find_all('tr')
    reference_size = trs[1].find('strong').text
    if trs[0].find('strong').string != "Porción:":
        raise NotFoundError('not table')
    
    tds = map(lambda x: x.find_all('td'), trs[2:])
    nutri_descriptors = map(
        lambda x: [x[0].text.strip().replace('\xa0', ' '), float(x[1].text)],
        tds
    )
    nutri_descriptors = list(map(lambda x: x + [x[0].split(' ')[-1][1:-1]], nutri_descriptors))
    return nutri_descriptors
