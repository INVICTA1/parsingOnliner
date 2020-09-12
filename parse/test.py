import requests
from bs4 import BeautifulSoup
import regex as re
from selenium import webdriver
import csv
from datetime import datetime, timedelta

flats = []


def parse_date(date_now, time=None):
    data_time = {
        'секунду,секунды,секунд': 1,
        'минуту,минуты,минут': 60,
        'час,часов,часа': 3600,
        'день,дня,дней': 86400,
        'неделя,недели,недель': 604800,
    }
    exam = ''
    try:
        words = time.split(' ')
        for key, value in data_time.items():
            if re.search(words[1].strip(), key):
                exam = value
        if not exam:
            return Exception
        if time.strip()=='час назад':
            return (date_now - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            return (date_now - timedelta(seconds=int(exam) * int(words[0]))).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return 'Not data'


def open_browser(chromedriver):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--incognito')
    browser = webdriver.Chrome(executable_path=chromedriver, options=options)
    browser.implicitly_wait(2)
    browser.maximize_window()
    return browser


def get_page(browser, url):
    browser.get(url)
    requiredHtml = browser.page_source
    soup = BeautifulSoup(requiredHtml, 'html.parser')
    return soup


def get_amount_pages(soup):
    amount_page = soup.select('.pagination-pages__item')[-1].text
    return amount_page


def parse_other_pages(browser, amount_page, url):
    for page in range(1, int(amount_page) + 1):
        print(f"Parse page {page} by {url + '#page=' + str(page)}...")
        soup = get_page(browser, url + '#page=' + str(page))
        for elem in soup.select('.classified'):
            dollar_price = ''
            rub_price = ''
            price = elem.select('.classified__price-value > span')
            time = elem.select('.classified__time')
            address = elem.select('.classified__caption-item_adress')
            for i in range(2):
                dollar_price = dollar_price + str(price[i].text.strip())
                rub_price = rub_price + str(price[i + 2].text.strip())
            flats.extend([['Prise USD: ' + dollar_price, 'Prise BYN: ' + rub_price,
                           'time: ', parse_date(datetime.now(), str(time[0].text.strip())),
                           'address: ' + address[0].text.strip()]])
    return flats


def save_result_csv(flats):
    path = r'..\resources\test.csv'
    with open(path, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for flat in flats:
            writer.writerow(flat)


def parseOnliner():
    URL = 'https://r.onliner.by/ak/'
    chromedriver = r'..\resources\chromedriver.exe'
    browser = open_browser(chromedriver)
    soup = get_page(browser, URL)
    amount_page = get_amount_pages(soup)
    flats = parse_other_pages(browser, amount_page, URL)
    print(flats)
    browser.quit()
    save_result_csv(flats)


parseOnliner()
