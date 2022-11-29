

def get_nutrition_data(parsed_html, url):
    table = parsed_html.find("table", class_='nutrition-table')
    if table:
        tbody = table.tbody.tbody
        trs = tbody.find_all('tr')
        nutri_descriptors = list(map(lambda x: x.find_all('td')[0].string, trs))
        nutri1.update(nutri_descriptors)
        return (0, nutri_descriptors)

    try:
        exit_code = 1
        browser = webdriver.Chrome(options=options, executable_path='C:/webdriver/chromedriver.exe')
        browser.get(url)
        timeout_in_seconds = 10
        WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.TAG_NAME, 'table')))
        html = browser.page_source
        soup = BeautifulSoup(html, features="html.parser")
        print(soup.find('table'))
        table = soup.find('table')
        tbody = table.tbody
        trs = tbody.find_all('tr')
        print(trs)
        if trs[0].find('strong').string != "Porción:":
            raise Exception('not table')
        
        nutri_descriptors = list(map(lambda x: x.find_all('td')[0].text.strip().replace('\xa0', ' '), trs[2:]))
        nutri2.update(nutri_descriptors)
        print(nutri_descriptors)

    except Exception:
        print("I give up...", url)
        exit_code = 2
    finally:
        #browser.quit()
        return (exit_code, )