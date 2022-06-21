import requests
from bs4 import BeautifulSoup


# URL для получения котировок на заданный день в формате XML
# Если в запросе отсутствует параметр ?date_req, то выдаётся последний зарезервированный документ

DOLLAR_RUB = 'https://www.cbr.ru/scripts/XML_daily.asp'


def get_current_price():

    """Функция делает запрос по URL и получает страницу в формате XML. 
    Возвращает значение, заключённое между тэгами <Value></Value> - 
    Дочерний тэг от тэга <Valute> с ID=R01235."""
    
    full_page = requests.get(DOLLAR_RUB)

    soup = BeautifulSoup(full_page.content, features='xml')
    value = str(soup.findAll('Valute', {'ID': 'R01235'}))

    first_tag, second_tag = value.find('<Value>') + len('<Value>'), value.find('</Value>')
    value = float(value.replace(',', '.')[first_tag: second_tag])

    return value