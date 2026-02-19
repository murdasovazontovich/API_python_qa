import pytest
import allure
from generators import generate_courier_payload
from methods.register_courier import RegisterCourier
from data import COURIER

class TestRegisterCourier:
    @allure.title("Создать курьера")
    def test_create_courier(self):
        payload = generate_courier_payload()
        response = RegisterCourier.create_courier(payload)

        assert response.status_code == 201  
        assert response.json() == {"ok": True}

    @allure.title("Нельзя дважды создать курьера")
    def test_create_twice_courier(self):
        RegisterCourier.create_courier(payload=COURIER)
        second_response = RegisterCourier.create_courier(payload=COURIER)
        assert second_response.status_code == 409
        assert second_response.json() == {"message": "Этот логин уже используется"}

    @allure.title("Неудачная попытка создать курьера без обязательного поля")
    @pytest.mark.parametrize("payload", [{"password": "12345", "firstName": "jnsbs"},
                                          {"login": "piojh", "firstName": "zdgf"},])
    def test_create_courier_missing_required_field(self, payload):
        response = RegisterCourier.create_courier(payload=payload)
        
        assert response.status_code == 400
        assert response.json() == {"message": "Недостаточно данных для создания учетной записи"}