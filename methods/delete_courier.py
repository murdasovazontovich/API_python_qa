import requests
import allure
from curl import URL



class DeleteCourier:
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(f"{URL.BASE_URL}/api/v1/courier/{courier_id}")
    
    @allure.step("Удаление курьера без айди")
    @staticmethod
    def delete_courier_without_id():
        return requests.delete(URL.DELETE_COURIER)  
