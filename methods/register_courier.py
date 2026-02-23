import requests
import allure
from curl import URL


class RegisterCourier:
    @allure.step("Зарегестрировать курьера")
    def create_courier(payload):
        return requests.post(URL.REGISTER_COURIER, json=payload)  
