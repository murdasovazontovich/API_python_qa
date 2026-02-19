import requests
import allure
from curl import URL


class GetOrder:
    @allure.step("Получить заказ")
    def get_order(self):
        return requests.get(URL.GET_ORDER)
