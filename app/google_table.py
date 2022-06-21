import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials


# Путь к файлу с API токенами
CREDENTIALS_FILE = 'app/creds.json'

# ID документа, с которым происходит работа
spreadsheet_id = '1xZVAOYe2m3h2mjNgrChbal2-i5c4W3KJK7zhQUvvaCU'


def get_sheets_values():

    """Функция возвращает значение словаря, соответствующее ключу "values" -
    - list записей из google sheets """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A2:D999',
        majorDimension='ROWS'
    ).execute()

    return (values["values"])
