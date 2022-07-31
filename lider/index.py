import sys
sys.path.append('../')

from scraper import get_product_data
from utils import build_nutrition_dict

with open('products_urls.txt', 'r', encoding='utf-8') as file:
    links = list(map(lambda x: x.strip(), file.readlines()))

for url in links[:1]:
    name, size, brand, nutrition_table = get_product_data(url)
    product = { "name": name, "brand": brand }
    print(product)
    nutrition = build_nutrition_dict(nutrition_table)
    print(nutrition)
    # send request
