import requests

from generate_schema import generate_schema


def get_data_for_schema_generation(method, url, body=None):
    """
    Получить данные для генерации схемы.
    :param method: тип запроса
    :param url: url метода
    :param body: тело запроса (при необходимости)
    :return: сгенерированный тест для Postman с json-схемой
    """
    if body is None:
        body = {}
    response = ''
    if method == 'GET':
        response = requests.get(url)
    if method == 'POST':
        response = requests.post(url, json=body)
    if method == 'PUT':
        response = requests.put(url, json=body)
    if method == 'PATCH':
        response = requests.patch(url, json=body)
    return generate_schema(response)

