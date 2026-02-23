import allure
from methods.delete_courier import DeleteCourier
from methods.register_courier import RegisterCourier
from methods.login_courier import LoginCourier
from generators import generate_courier_payload

class TestDeleteCourier:
    @allure.title("Удаление курьера")
    def test_create_delete_courier(self, created_courier_and_delete):
        delete_response = DeleteCourier.delete_courier(created_courier_and_delete)

        assert delete_response.status_code == 200
        assert delete_response.json() == {"ok": True}

    @allure.title("Удаление курьера без айди")
    def test_delete_courier_without_id(self):
        delete_response = DeleteCourier.delete_courier_without_id()

        assert delete_response.status_code == 400
        assert delete_response.json() == {"message":  "Недостаточно данных для удаления курьера"}

    @allure.title("Удаление курьера которого не существует")
    def test_delete_non_existing_id(self, create_courier):
        DeleteCourier.delete_courier(create_courier)
        response = DeleteCourier.delete_courier(create_courier)

        assert response.status_code == 404
        assert response.json() == {"message": "Курьера с таким id нет"}        