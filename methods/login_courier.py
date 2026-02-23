import requests
import allure
from curl import URL


class LoginCourier:
    @allure.step("Залогиниться курьеру")
    def login_courier(payload):
        return requests.post(URL.LOGIN_COURIER, json=payload)
