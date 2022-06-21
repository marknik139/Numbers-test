# Numbers - Тестовое задание

# Содержание
1. [Описание работы сервиса](#descr)
2. [Описание реализации](#realiz)
3. [Запуск](#run)
4. [Работа сервиса](#work)


## Описание работы сервиса <a name="descr"></a>
Необходимо разработать скрипт на языке Python 3, 
который будет выполнять следующие функции:

- Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1LTejK-Oo7L1bFreBIIcEZnF1W1RCC1s_jos3EuIP0jI/edit?usp=sharing) (необходимо копировать в свой Google аккаунт и выдать самому себе права).

- Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»

    + Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    
    + Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
- Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).


## Описание реализации <a name="realiz"></a>

|     |     |
| --- | --- |
| Бэкенд | Python, GoogleAPI, BeautifulSoup, oauth2client, psycopg2 |
| СУБД | PostgreSQL |

**app/ - корень приложения**  

**main.py:**  

- rewrite_database реализует перезапись актуального содержимого *БД*

**parser.py:**  

- get_current_price делает запрос по URL и получает данные с XML страницы  

**google_table.py:**

- get_sheets_values получает значения из таблицы *Google Sheets*

**converter.py:**

- convert_values значения из таблицы *Google Sheets* в необходимый формат


**config.py:**

- Файл с параметрами подключения к PostgreSQL

**check.py:**

- check_changes проверяет наличие изменения таблицы google sheets и курса валюты на сайте ЦБ


## Запуск <a name="run"></a>

1. Установить Python 3.10 или выше
2. Создать виртуальное окружение, активировать его и установить зависомости:
```
python3.10 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
3. Установить PostgreSQL, создать базу данных. Установить необходимые параметры подключения в *config.py*
4. Запустить сервис из директории app/
```
.../app/main.py
```
5. <a href="https://docs.google.com/spreadsheets/d/1xZVAOYe2m3h2mjNgrChbal2-i5c4W3KJK7zhQUvvaCU/edit#gid=0">Ссылка на мой Google Sheets<a>
  
   - Пользователю sales@numbersss.com предоставлены права редактора документа

## Работа сервиса <a name="work"></a>
  
  Таблица Google Sheets:
  
  <img width="341" alt="image" src="https://user-images.githubusercontent.com/60853743/174830955-d2be2b5e-a080-4011-b6f7-df696bcc87b4.png">
  
  Таблица pgAdmin:
  
  <img width="368" alt="image" src="https://user-images.githubusercontent.com/60853743/174830602-e7f37a3b-f3a7-41ac-ad2d-f15a8c8f09c6.png">


  **Для обновление таблицы в pgAdmin: table name -> Просмотр -> Все строки** 
  
  <img width="475" alt="image" src="https://user-images.githubusercontent.com/60853743/174831473-67ac32f9-87d4-4cae-892b-1ede0c14287b.png">
