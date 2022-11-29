from math import prod
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
    info = product_detail.find('h1', class_='product-name').text
    name = ' '.join(info.split(' ')[:-2])
    size = ' '.join(info.split(' ')[-2:])
    brand = product_detail.find('a', class_='product-brand').text
    nutrition_table = get_nutrition(product_detail)
    portion = get_portion(product_detail)
    amount = int(portion.split('(')[-1].split(' ')[0])
    return name, size, brand, nutrition_table, portion, amount

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
