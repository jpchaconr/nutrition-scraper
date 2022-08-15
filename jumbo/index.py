import sys
sys.path.append('../')

from scraper import get_product_data
from utils import build_nutrition_dict
from utils_requests import AuthRequests, ProductRequests, NutritionRequests
import settings

auth = AuthRequests()
product_request = ProductRequests()
nutrition_request = NutritionRequests()

rut = settings.USER_RUT
password = settings.USER_PASSWORD

country = settings.COUNTRY

auth_response = auth.login(rut, password)
access = auth_response.json()["access"]

with open('products_urls.txt', 'r', encoding='utf-8') as file:
    links = list(map(lambda x: x.strip(), file.readlines()))

for url in links[50:]:
    print('----\n' + url + '----\n')
    error = False
    for attempt in range(3):
        try:
            name, size, brand, nutrition_table = get_product_data(url)
        except Exception as e:
            error = True
            print(f'Error ({attempt}):', url)
            continue
        error = False
        break

    if error:
        continue

    product = { "name": name, "brand": brand, "country": country }
    nutrition = build_nutrition_dict(nutrition_table)
    print(nutrition)
    
    # SEND REQUESTS
    # Product
    product_response = product_request.add_product(product, access)
    product_data = product_response.json()
    print(product_data)
    try:
        product_id = product_data["id"]
    except:
        # print(product_data)
        continue

    # Nutrition
    nutrition["product"] = product_id
    nutrition["product_measure"] = "100 (ml o g)"
    nutrition_response = nutrition_request.add_nutrition(nutrition, access)
    print(nutrition_response.json())
    #nutrition_data = nutrition_response.json()
