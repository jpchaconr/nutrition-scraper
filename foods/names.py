from math import prod
from bs4 import BeautifulSoup
import requests

OUTPUT_FILE = 'food_info2.txt'

file = open('nutritions2.txt', encoding='utf-8')
names_file = open('food_info.txt', encoding='utf-8')

def write_food_info(file, url, name, nutrition):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(url + '\n')
        f.write(name + '\n')
        f.write(nutrition + '\n')

def extract_name(url):
    req = requests.get(url)
    food_page = BeautifulSoup(req.text, 'html.parser')
    name = food_page.find('h1').text.strip()
    return name

reset = open(OUTPUT_FILE, 'w', encoding='utf-8')
reset.close()

url = file.readline().strip()
url2 = names_file.readline().strip()
while url != '':
    assert url == url2
    nutri = file.readline().strip()
    name = names_file.readline().strip()
    names_file.readline().strip()
    # name = extract_name(url)
    print(url, name)
    print('----------------------')
    write_food_info(OUTPUT_FILE, url, name, nutri)

    url = file.readline().strip()
    url2 = names_file.readline().strip()
