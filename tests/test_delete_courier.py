import allure
from methods.delete_courier import DeleteCourier
from methods.register_courier import RegisterCourier
from methods.login_courier import LoginCourier
from generators import generate_courier_payload

class TestDeleteCourier:
    @allure.title("Удаление курьера")
    def test_create_delete_courier(self):
        courier = generate_courier_payload()
        RegisterCourier.create_courier(courier)
        login_response = LoginCourier.login_courier({"login": courier["login"], "password": courier["password"]})
        courier_id = login_response.json()["id"]
        delete_response = DeleteCourier.delete_courier(courier_id)

        assert delete_response.status_code == 200
        assert delete_response.json() == {"ok": True}

    @allure.title("Удаление курьера без айди")
    def test_delete_courier_without_id(self):
        delete_response = DeleteCourier.delete_courier_without_id()

        assert delete_response.status_code == 400
        assert delete_response.json() == {"message":  "Недостаточно данных для удаления курьера"}

    @allure.title("Удаление курьера которого не существует")
    def test_delete_non_existing_id(self):
        courier = generate_courier_payload()
        RegisterCourier.create_courier(courier)
        login_r = LoginCourier.login_courier({"login": courier["login"], "password": courier["password"]})
        courier_id = login_r.json()["id"]
        DeleteCourier.delete_courier(courier_id)
        response = DeleteCourier.delete_courier(courier_id)

        assert response.status_code == 404
        assert response.json() == {"message": "Курьера с таким id нет"}        