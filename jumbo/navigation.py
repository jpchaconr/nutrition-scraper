from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_products_links():
    timeout_in_seconds = 10
    WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'ul.shelf-list')))
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")
    links = list(map(lambda x: x.find('a', class_='shelf-product-title')['href'], soup.find_all('li', class_='shelf-item')))
    return list(map(lambda x: 'https://www.jumbo.cl' + x, links))

def write_new_links(file_name, links):
    with open(file_name, 'a') as file:
        file.write('\n'.join(links))

sections = [
    'https://www.jumbo.cl/lacteos',
    'https://www.jumbo.cl/despensa',
    'https://www.jumbo.cl/frutas-y-verduras',
    'https://www.jumbo.cl/carniceria',
    'https://www.jumbo.cl/bebidas-aguas-y-jugos',
    'https://www.jumbo.cl/congelados',
    'https://www.jumbo.cl/desayuno-y-dulces',
    'https://www.jumbo.cl/comidas-preparadas',
    'https://www.jumbo.cl/quesos-y-fiambres',
    'https://www.jumbo.cl/pescaderia',
    'https://www.jumbo.cl/mundo-bio-natura'
]

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(service=Service('C:/webdriver/chromedriver.exe'), options=options)

for section in sections[2:]:
    print(section)
    print("##############\n"*3)
    browser.get(section)
    links = get_products_links()
    try:
        write_new_links('products_urls.txt', links)
    except:
        print("Something went wrong in page 0")

    pages_btns = browser.find_elements(By.CLASS_NAME, 'page-number')
    next_page_index = 1
    while next_page_index < len(pages_btns):
        browser.execute_script("arguments[0].click();", pages_btns[next_page_index])
        links = get_products_links()
        try:
            write_new_links('products_urls.txt', links)
        except:
            print("Something went wrong in page", next_page_index)

        print(next_page_index)
        pages_btns = browser.find_elements(By.CLASS_NAME, 'page-number')
        next_page_index += 1
