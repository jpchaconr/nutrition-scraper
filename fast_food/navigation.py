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

main_url = 'https://www.mcdonalds.cl/productos'

options = Options()
# options.add_argument('--headless')

def navigate_products():
    browser = webdriver.Chrome(service=Service('C:/webdriver/chromedriver.exe'), options=options)
    categories = get_categories_urls(main_url, browser)
    for link in categories:
        if link.get_attribute('href') == "https://www.mcdonalds.cl/productos/cajita-feliz":
            save_products_urls('files/prods_urls.txt', "https://www.mcdonalds.cl/productos/cajita-feliz")
            continue

        print(link.get_attribute('href'))
        browser.execute_script("arguments[0].click();", link)
        sleep(2)
        products = get_products_urls(browser)
        save_products_urls('files/prods_urls.txt', products)

def get_categories_urls(url, browser):
    browser.get(url)
    sleep(5)

    div = browser.find_element(By.ID, "categoriesMenu")
    categories_links = div.find_elements(By.TAG_NAME, "a")
    return categories_links[1:]

def get_products_urls(browser):
    nav = browser.find_element(By.XPATH, "//nav[contains(@class, 'mcd-category-detail')]")
    products = nav.find_elements(By.TAG_NAME, 'a')
    products_urls = []
    for product in products:
        products_urls.append(product.get_attribute('href'))
    return products_urls

def save_products_urls(file_name, products):
    if isinstance(products, str):
        with open(file_name, 'a+') as file:
            file.write(products + '\n')
        return

    with open(file_name, 'a+') as file:
        print('write')
        for prod in products:
            file.write(prod + '\n')

navigate_products()
