import requests
import configuration
import data

# Функция для создания нового заказа
def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers
    )

# Функция для получения данных заказа по его трек-номеру
def get_order_by_track(track_number):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params={"t": track_number}
    )