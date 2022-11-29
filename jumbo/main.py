import sys
import time
sys.path.append('../')

from jumbo.scraper import get_product_data
from utils import build_nutrition_dict
from error_handler import ErrorHandler
from logger import Logger

country = 'Chile'
log_file = str(int(time.time()))
log = Logger(f'logs/{log_file}.txt')

class Scrapper:
    def __init__(self, access, product, nutrition) -> None:
        pass
        with open('products_urls.txt', 'r', encoding='utf-8') as file:
            self.links = list(map(lambda x: x.strip(), file.readlines()))

    def post_products(self):
        for url in self.links:
            print('--------\n', url, '\n--------\n')
            try:
                self.post_product(url)
            except Exception as e:
                log.error('POST', url)
                print('ERROR:', url)
            print()

    def post_product(self, url):
        errorHandler = ErrorHandler(retry=3)
        name, size, brand, nutrition_table, portion, amount = errorHandler.execute(get_product_data, url)
        amount = int(portion.split('(')[-1].split(' ')[0])

        product = { "name": name, "brand": brand, "country": country }
        # product_response = self.product.add_product(product, self.access)
        # product_data = product_response.json()
        # product_id = product_data["id"]

        nutrition = build_nutrition_dict(nutrition_table)
        # nutrition["product"] = product_id
        nutrition["product_measure"] = "100 (ml o g)"
        # nutrition_response = self.nutrition.add_nutrition(nutrition, self.access)
        # nutrition_data = nutrition_response.json()

        # nutrition_id = nutrition_data["id"]
        # measure = { "name": portion, "amount": amount }
        # measure_response = self.nutrition.add_measure(nutrition_id, measure, self.access)

scraper = Scrapper(1,2,3)
scraper.post_products()
