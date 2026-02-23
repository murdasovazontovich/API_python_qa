import requests
import allure
from curl import URL


class CreateOrder:
    @allure.step("Создание  заказа")
    def create_order(payload):
        return requests.post(URL.CREATE_ORDER, json=payload)
