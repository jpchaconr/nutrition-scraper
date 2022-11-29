import sys
import time
sys.path.append('../')

from scraper import get_product_data
from utils import build_nutrition_dict
from utils_requests import AuthRequests, ProductRequests, NutritionRequests
from error_handler import ErrorHandler
from logger import Logger
import settings

# auth = AuthRequests()
# product_request = ProductRequests()
# nutrition_request = NutritionRequests()

rut = settings.USER_RUT
password = settings.USER_PASSWORD

country = settings.COUNTRY

# auth_response = auth.login(rut, password)
# access = auth_response.json()["access"]

# error_handler = ErrorHandler(3)
log_file = str(int(time.time()))
log = Logger(f'logs/{log_file}.txt')

with open('products_urls.txt', 'r', encoding='utf-8') as file:
    links = list(map(lambda x: x.strip(), file.readlines()))

portions = set()
i= 0

for url in links[:10]:
    i+=1
    print('----\n' + url + '  ' + str(i) + '  ' + '\n----\n')
    error = False
    for attempt in range(3):
        try:
            name, size, brand, nutrition_table, portion, amount = get_product_data(url)
            portions.add(portion)
        except Exception as e:
            error = True
            print(f'Error ({attempt}):', url)
            continue
        error = False
        break

    if error:
        log.error('POST', url)
        continue

    product = { "name": name, "brand": brand, "country": country }
    nutrition = build_nutrition_dict(nutrition_table)
    measure = { "name": portion, "ammount": amount }
    
    # SEND REQUESTS
    # Product
    print(product)
    break
    product_response = product_request.add_product(product, access)
    try:
        product_data = product_response.json()
        product_id = product_data["id"]
    except:
        print(product_data)
        log.error('PRODUCT ID ', f' {str(product_data)} ({url})')
        continue

    # Nutrition
    nutrition["product"] = product_id
    nutrition["product_measure"] = "100 (ml o g)"
    nutrition_response = nutrition_request.add_nutrition(nutrition, access)
    try:
        nutrition_data = nutrition_response.json()
        nutrition_id = nutrition_data["id"]
    except:
        print(nutrition_data)
        log.error('NUTRITION ID ', f' {str(nutrition_data)} ({url})')
        log.info('PROD ID ', f' {product_id}')
        continue

    # nutrition_id ='162e4566-b802-4f37-b393-eda2e9f8fe16'
    measure_response = nutrition_request.add_measure(nutrition_id, measure, access)
    try:
        measure_data = measure_response.json()
        measure_id = measure_data["ammount"]
    except:
        print(measure_data)
        log.error('MEASURE ID ', f' {str(measure_data)} ({url})')
        log.info('PROD ID ', f' {product_id}')
        continue

    print()
