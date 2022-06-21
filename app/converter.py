from datetime import datetime

from google_table import get_sheets_values
from parser import get_current_price


def convert_values():

    """Функция получает на вход list записей из google sheets и преобразовывает
    их к нужному типу из string для вставки в PostgreSQL.
    Если срок поставки"""


    course = get_current_price()

    converted = get_sheets_values()
    for i in range(len(converted)):
        converted[i][0] = int(converted[i][0])
        converted[i][1] = int(converted[i][1])
        converted[i][2] = int(converted[i][2])
        converted[i].insert(3, converted[i][2] * course)
        converted[i][3] = round(converted[i][3], 2)
        converted[i][4] = datetime.strptime(converted[i][4], '%d.%m.%Y').date()

    return converted

