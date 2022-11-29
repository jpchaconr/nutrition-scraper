import json
from pkgutil import get_data
from bs4 import BeautifulSoup

from nutrition_extractor import strategy

food_list = open('tables_nutrition.html', encoding='utf8')
foods_nutrition = open('nutritions2.txt', 'w', encoding='utf-8')

def read_list_item(list_file):
    line = list_file.readline().strip('\n')
    item = ''
    while line != '':
        item += line + '\n'
        line = list_file.readline().strip('\n')
        if '<h4>' in line:
            yield item
            item = ''
    yield item

i = 0
for item in read_list_item(food_list):
    print(i)
    i += 1

    food = BeautifulSoup(item, 'html.parser')
    nutritions = {}

    url = food.find('h4').text
    foods_nutrition.write(url + '\n')

    for b_tag in food.find_all('b'):
        nutrition_desc = b_tag["itemprop"]
        measure = float(b_tag.text.strip())
        add_nutrition = strategy.get(nutrition_desc, lambda x, y: "Invalid")
        add_nutrition(nutritions, measure)

    foods_nutrition.write(json.dumps(nutritions) + '\n');

foods_nutrition.close()
