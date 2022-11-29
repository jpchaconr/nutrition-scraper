from bs4 import BeautifulSoup

base_url = 'https://comoquiero.net'
food_list = open('list.html', encoding='utf8')

def read_list_item(list_file):
    line = list_file.readline().strip('\n')
    item = ''
    while line != '':
        line = list_file.readline().strip('\n')
        if '<li' in line:
            item  = line
        else:
            item += '\n' + line
        
        if '</li' in line:
            yield item

food_urls = open('foods_urls.txt', 'w')

for item in read_list_item(food_list):
    food = BeautifulSoup(item, 'html.parser')

    try:
        food_url = base_url + food.find('a', { "class": "recipe-name" })['href']
        food_urls.write(food_url + '\n')
    except:
        print('No url found')

food_urls.close()
food_list.close()
