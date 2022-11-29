import json
import math
import sys
import time
from unicodedata import name
sys.path.append('../')
from logger import Logger

from utils_requests import AuthRequests, ProductRequests, NutritionRequests
from utils import build_nutricion_dict
import settings

auth = AuthRequests()
product_request = ProductRequests()
nutrition_request = NutritionRequests()

rut = settings.USER_RUT
password = settings.USER_PASSWORD

country = settings.COUNTRY

auth_response = auth.login(rut, password)
access = auth_response.json()["access"]

log_file = str(int(time.time()))
log = Logger(f'logs/{log_file}.txt')

nutrition_info_file = 'files/products_info.txt'

with open(nutrition_info_file, 'r', encoding='utf-8') as file:
    foods = []
    nutrition = file.readline().strip()
    while nutrition != '':
        nutrition = json.loads(nutrition)
        foods.append(nutrition)
        nutrition = file.readline().strip()

i = 0
for food in foods:
    if len(food['nutrition']) == 0 or food['nutrition'][0][1] == 0:
        continue

    print(i)
    i += 1
    print(food['name'])

    measure = { "name": "1 Unidad", "ammount": food['nutrition'][0][1] }
    nutrition = build_nutricion_dict(food['nutrition'])

    product = { "name": food['name'], "brand": food['brand'], "country": country, "product_type": 2 }
    product_response = product_request.add_product(product, access)
    product_data = product_response.json()
    try: 
        product_id = product_data["id"]
    except:
        print(product_data)
        log.error('Create product', f'{str(product_data)} | {name}')
        continue

    print(product_id)
    nutrition["product"] = product_id
    nutrition["product_measure"] = "100 (ml o g)"
    nutrition_response = nutrition_request.add_nutrition(nutrition, access)
    try:
        nutrition_data = nutrition_response.json()
        nutrition_id = nutrition_data["id"]
    except:
        print(nutrition_data)
        log.error('NUTRITION ID ', f' {str(nutrition_data)} ({name})')
        log.info('PROD ID ', f' {product_id}')
        continue

    measure_response = nutrition_request.add_measure(nutrition_id, measure, access)
    try:
        measure_data = measure_response.json()
        measure_id = measure_data["ammount"]
    except:
        print(measure_data)
        log.error('MEASURE ID ', f' {str(measure_data)}')
        log.info('PROD ID ', f' {product_id}')
        continue

    print('-----------------------------\n')
    print()
