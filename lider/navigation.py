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

categories = [
    "Carnes y Pescados",
    "Congelados",
    "Frutas y Verduras",
    "Frescos y Lácteos",
    "Platos Preparados",
    "Panadería y Pasteleria",
    "Desayuno y Dulces",
    "Colaciones",
    "Despensa",
    "Bebidas y Licores",
]

super = 'https://www.lider.cl/supermercado/'

sections_urls_file = open('sections_urls.txt', 'w')

options = Options()
# options.add_argument('--headless')
browser = webdriver.Chrome(service=Service('C:/webdriver/chromedriver.exe'), options=options)

browser.get(super)

sleep(5)
categories_btn = browser.find_element("xpath", "//button[@data-testid='menu-button-test-id']")
browser.execute_script("arguments[0].click();", categories_btn)
print(categories_btn)
sleep(2)

for i in range(len(categories)):
    divvv = browser.find_element("xpath", f"//div[contains(text(), '{categories[i]}')]")
    browser.execute_script("arguments[0].click();", divvv)
    print(divvv)
    sleep(2)

    # styled__ThirdLevelSection
    list = browser.find_elements("xpath", "//div[contains(@class, 'styled__ThirdLevelSection')]/div")
    print(list)
    print(len(list))
    sleep(2)
    for div_element in list:
        a = div_element.find_element(By.TAG_NAME, "a")
        print(a.get_attribute('href'))
        sections_urls_file.write(a.get_attribute('href') + '\n')

sections_urls_file.close()

class Navigation:
    def __init__(self, categories) -> None:
        self.categories = categories
        self.categories_file_name= "categories_urls.txt"
        self.products_file_name = "products_urls2.txt"
        self.super = 'https://www.lider.cl/supermercado/'

    def start_scraper(self):
        options = Options()
        # options.add_argument('--headless')
        self.browser = webdriver.Chrome(service=Service('C:/webdriver/chromedriver.exe'), options=options)
        self.browser.get(self.super)

    def get_categories_urls(self):
        sleep(5)
        categories_btn = browser.find_element("xpath", "//button[@data-testid='menu-button-test-id']")
        browser.execute_script("arguments[0].click();", categories_btn)
        print(categories_btn)

        subcategories = []
        for category in self.categories:
            subcategories += self.get_subcategories(category)

        sleep(2)
        urls = map(lambda x: x.find_element(By.TAG_NAME, "a").get_attribute('href'), subcategories)
        return urls

    def get_subcategories(self, category):
        divvv = browser.find_element("xpath", f"//div[contains(text(), '{category}')]")
        browser.execute_script("arguments[0].click();", divvv)
        print(divvv)
        sleep(2)

        # styled__ThirdLevelSection
        list = browser.find_elements("xpath", "//div[contains(@class, 'styled__ThirdLevelSection')]/div")
        div_element.find_element(By.TAG_NAME, "a")
        print(list)
        print(len(list))
        sleep(2)
        return list

    def get_products_urls(self):
        pass
