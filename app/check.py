from parser import get_current_price
from google_table import get_sheets_values
import time


def check_changes():

    """Функция проверяет наличие изменения таблицы google sheets и курса валюты на сайте ЦБ.
    В случае обнаружения любого из изменений возвращает True. Задержка необходима для корректной
    работы Google API"""

    value_price = get_current_price()
    value_table = get_sheets_values()

    while (True):
        
        time.sleep(1)
        new_value_price = get_current_price()
        new_value_table = get_sheets_values()

        if value_price != new_value_price or value_table != new_value_table:
            value_price = new_value_price
            value_table = new_value_table

            return True