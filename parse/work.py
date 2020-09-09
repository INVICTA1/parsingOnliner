import requests
from bs4 import BeautifulSoup


def parse_storgame():
    URL = 'https://stopgame.ru/topgames'
    r = requests.get(URL)
    html = BeautifulSoup(r.content, 'html.parser')
    for elem in html.select('.game-summary-horiz'):
        title = elem.select('.caption > a')
        print(title[0].text)


def parse_onliner():
    URL = 'https://r.onliner.by/ak/?rent_type%5B%5D=room&only_owner=true#bounds%5Blb%5D%5Blat%5D=53.89129696150157&bounds%5Blb%5D%5Blong%5D=27.304834215169524&bounds%5Brt%5D%5Blat%5D=53.960988463831015&bounds%5Brt%5D%5Blong%5D=27.75315394037773'
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'params': '*/*'}
    r = requests.get(URL, headers=HEADERS, params=None)

    html = BeautifulSoup(r.content, 'html.parser')
    print(html)
    # for elem in html.select('.classified > a'):
    #     print(elem)
    # for elem in html.select('.classified'):
    #     print(elem)
    items = html.find_all('a', class_='classified')
    # price = elem.select('.classified__price classified__price_secondary')
    # time = elem.select('.classified__time > a')
    # adress = elem.select('.classified__caption-item classified__caption-item_adress')
    # print(time.text, price, adress)


def selenium():
    from selenium import webdriver
    flats = []
    URL = 'https://r.onliner.by/ak/'
    chromedriver = 'resources\chromedriver.exe'
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('--incognito')
    browser = webdriver.Chrome(executable_path=chromedriver, options=options)
    browser.implicitly_wait(2)
    browser.maximize_window()
    browser.get(URL)
    requiredHtml = browser.page_source
    soup = BeautifulSoup(requiredHtml, 'html.parser')

    pagination = soup.select('.pagination-pages__item')[-1].text
    print(pagination)
    requiredHtml = browser.page_source
    soup = BeautifulSoup(requiredHtml, 'html.parser')
    for elem in soup.select('.classified'):
        dollar_price = ''
        rub_price = ''
        price = elem.select('.classified__price-value > span')
        time = elem.select('.classified__time')
        address = elem.select('.classified__caption-item_adress')
        for i in range(2):
            dollar_price = dollar_price + str(price[i].text.strip())
            rub_price = rub_price + str(price[i + 2].text.strip())
        flats.extend(['Prise:', dollar_price, 'or', rub_price, 'time:', time[0].text.strip(), 'address:',
                      address[0].text.strip()])
        # print('Prise:', dollar_price,'or' ,rub_price, 'time:', time[0].text.strip(), 'address:', address[0].text.strip())

    browser.quit()
    for i in flats:
        print(i)


selenium()
