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

from utils import nutrition_type_map, split_measure_unit

PRODUCTS_URLS_FILE = "files/prods_urls.txt"
PRODUCTS_NUTRITION_FILE = "files/products_info.txt"

options = webdriver.ChromeOptions()
options.add_argument('--headless')

def navigate_products():
    browser = webdriver.Chrome(options=options, executable_path='C:/webdriver/chromedriver.exe')

    with open(PRODUCTS_URLS_FILE, 'r') as file:
        products_urls = file.readlines()

    for url in products_urls:
        browser.get(url)
        sleep(5)
        table = browser.find_elements(By.CLASS_NAME, 'mcd-nutritional-information__table-row')

        name = browser.find_element(By.TAG_NAME, 'h1').text
        brand = "mcdonalds"
        nutrition = []
        for row in table:
            cols = row.find_element(By.CLASS_NAME, 'columns')
            try:
                nutrition_attr = build_nutrition_attr(cols)
                nutrition.append(nutrition_attr)
            except:
                pass

        save_product_nutrition(name, brand, nutrition)

def build_nutrition_attr(cols):
    nutrition_type = cols.find_element(By.CLASS_NAME, 'mcd-nutritional-information__type').get_attribute("innerHTML")
    info = cols.find_elements(By.TAG_NAME, 'div')[1].find_element(By.TAG_NAME, 'span')
    measure_unit = split_measure_unit(info.get_attribute("innerHTML"))
    return [nutrition_type_map[nutrition_type], *measure_unit]

def save_product_nutrition(name, brand, nutrition):
    with open(PRODUCTS_NUTRITION_FILE, 'a+', encoding='utf-8') as file:
        product_info = { "name": name, "brand": brand, "nutrition": nutrition }
        file.write(json.dumps(product_info, ensure_ascii=False))
        file.write('\n')

navigate_products()
